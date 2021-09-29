from PIL import Image
import sys
import random
import glob

ITERATIONS = 300
CORRECTION = 2.0
WEIGHT_HUE = 0.500
WEIGHT_SATURATION = 0.500
WEIGHT_VALUE = 0.500

def color_distance(c1, c2):
	# Determines distance between two colors	
	dist_hue =			((c1[0]-c2[0])**CORRECTION) * WEIGHT_HUE
	dist_saturation =	((c1[1]-c2[1])**CORRECTION) * WEIGHT_SATURATION
	dist_value =		((c1[2]-c2[2])**CORRECTION) * WEIGHT_VALUE
	
	return dist_hue + dist_saturation + dist_value


def image_distance(im1, im2):
	# Determines how different the two images are from each other
	width, height = im1.size
	
	total = 0
	for x in range(width):
		for y in range(height):
			c1 = im1.getpixel((x, y))
			c2 = im2.getpixel((x, y))
			total += color_distance(c1,c2)
	
	return total/(width*height)


def pick_random_palette(im, count):
	# Picks a random selection of colors from the image
	width, height = im.size
	
	list = []
	for i in range(count):
		x = random.randint(0, width-1)
		y = random.randint(0, height-1)
		list.append(im.getpixel((x, y)))
	
	return list


def get_palette(im, count):
	# Determines the best palette for the image by trying out many possible palettes
	best_palette = [0,0,0]
	best_distance = sys.maxsize

	for i in range(ITERATIONS):
		# Generate random palette
		palette = pick_random_palette(im, count)
		im_compare = palettize(im, palette)
		distance = image_distance(im, im_compare)
		
		# See if it's the best
		if distance < best_distance:
			best_distance = distance
			best_palette = palette
	
	return best_palette

def palettize(im, palette):
	# Palettizes an image to a palette
	
	im = im.copy()
	width, height = im.size
	
	for x in range(width):
		for y in range(height):
			# Find the closest palette color to the pixel's color
			best_index = 0
			best_distance = sys.maxsize
			
			# Also track second closest for dithering
			second_index = 0
			second_distance = sys.maxsize
			
			cur_color = im.getpixel((x, y))
			
			# Loop through palette colors
			for c in range(len(palette)):
				distance = color_distance(cur_color, palette[c])
				if (distance < best_distance):
					second_distance = best_distance
					second_index = best_index
					
					best_distance = distance
					best_index = c
			
			'''
			# Dithering
			choice = best_index
			if dithering:
				# Randomly pick between the two nearest pixels
				# Weights towards closer one
				ri = random.random()
				ratio = second_distance/(best_distance+second_distance)
				if (ri < ratio):
					choice = second_index
			'''
			
			# Write the pixel
			im.putpixel((x, y), palette[best_index])
	
	return im

def main():
	# Handle command-line input
	if len(sys.argv) < 2 or len(sys.argv) > 3:
		print(f"Usage: {sys.argv[0]} [num_colors] *[myimage.png]")
		print("[myimage] will be palettized to [num_colors] colors")
		print("Leave [myimage.png] blank to palettize all images in the folder")
		exit(1)
	
	# Parse other command-line stuff
	try:
		num_colors = int(sys.argv[1])
	except:
		print("Error: [num_colors] must be an integer")
		exit(1)
	
	# Generate file path list
	path_list = []
	if len(sys.argv) == 3:
		path_list.append(sys.argv[2])
	else:
		path_list =  glob.glob("*.png")
		path_list += glob.glob("*.jpg")
		path_list += glob.glob("*.jpeg")
		path_list += glob.glob("*.bmp")
		path_list += glob.glob("*.gif")
		# Safeguard to prevent palettizing images multiple times
		safe_list = []
		for item in path_list:
			if ("_palettized_" not in item):
				safe_list.append(item)
		path_list = safe_list
	
	print(path_list)
				
	
	# Iterate through images
	for im_path in path_list:
		# Load the image
		im = Image.open(im_path)
		hsv_im = im.convert('HSV')
		
		# Iterate through attempts
		for i in range(8):
			# Find the image's palette
			pal = get_palette(hsv_im, num_colors)
			
			# Palettize the image
			im_final = palettize(hsv_im, pal)
			
			# Generate file path
			path_split = im_path.split(".")
			ins = len(path_split)-2
			if ins < 0:
				ins = 0
			path_split[ins] += "_palettized_" + str(i+1)
			output_path = ""
			for p in path_split:
				output_path += p
				output_path += "."
			output_path = output_path[:-1]
			
			# Save to file
			print(output_path)
			im_final = im_final.convert('RGB')
			im_final.save(output_path, "PNG")

main()



