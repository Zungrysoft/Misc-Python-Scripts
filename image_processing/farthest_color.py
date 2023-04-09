# Script for analyzing color palettes and spotting potential missing colors you might want to add

from PIL import Image
import sys
import math

SKIP_HUE = 5
SKIP = 10

WEIGHT_HUE = 1
WEIGHT_SAT = 1
WEIGHT_VAL = 1

ITERATIONS = 15

def convert_hsv_scale(hsv):
    return (
        int(hsv[0]*(360/255)),
        int(hsv[1]*(100/255)),
        int(hsv[2]*(100/255))
    )

def hsv_dist(a, b):
    # Figure out linear distances of each component
    h_dist = min(min(abs(a[0]-b[0])*WEIGHT_HUE, abs((a[0]+256)-b[0])*WEIGHT_HUE), abs((a[0]-256)-b[0])*WEIGHT_HUE)
    s_dist = (a[1]-b[1])*WEIGHT_SAT
    v_dist = (a[2]-b[2])*WEIGHT_VAL

    # Scale down hue and saturation when value is low
    # When value is 0, hue and saturation have no effect on the result
    v_scale = ((a[2]+b[2]) / 2) / 255
    h_dist *= v_scale
    s_dist *= v_scale

    # Scale down hue when saturation is low
    s_scale = ((a[1]+b[1]) / 2) / 255
    h_dist *= s_scale

    # Calculate euclidean distance
    dist = h_dist**2 + s_dist**2 + v_dist**2
    return dist

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} [image.png]")
        return

    # Open the image and convert to hsv
    im_path = sys.argv[1]
    im = Image.open(im_path)
    im = im.convert('HSV')
    pixels = im.load()
    width = im.width
    height = im.height

    # Create set of all colors in the image
    colors = set()
    for y in range(height):
        for x in range(width):
            colors.add(pixels[x, y])
    

    # We will perform this process several times. We find the farthest color, add it to the list,
    # then find the next farthest color away
    print("Farthest colors in (HSV) scale are:")
    added_colors = []
    for i in range(ITERATIONS):
        # Iterate over all possible colors and find the farthest one
        # We're trying to find which color is FARTHEST away from its CLOSEST pixel in the image
        # That way, we find the color that's the farthest from every other color
        farthest_distance = 0
        farthest_color = (0, 0, 0)
        for h in range(0, 255, SKIP_HUE):
            for s in range(0, 255, SKIP):
                for v in range(0, 255, SKIP):
                    # Find the pixel which is closest to this one
                    closest_distance = 999999999999
                    closest_color = (0, 0, 0)

                    for color in colors:
                        dist = hsv_dist(color, (h, s, v))
                        
                        if dist < closest_distance:
                            closest_distance = dist
                            closest_color = (h, s, v)
                    
                    if closest_distance > farthest_distance:
                            farthest_distance = closest_distance
                            farthest_color = closest_color

        # Add the color to the list of colors
        colors.add(farthest_color)
        print(convert_hsv_scale(farthest_color))

main()