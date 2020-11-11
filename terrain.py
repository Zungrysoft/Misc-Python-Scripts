#A simple python implementation of the Diamond-Square terrain generator algorithm
#I wrote it to gain a proper understanding of the algorithm before I attempted the herculean task of implementing it mcfunction
#Written by ZungryWare

import random
import sys

#Visualizes a space on the table with an ascii character
def printitem(v):
	t = [0,1,2,3,4,5,6,7,8]
	c = [' ','.',':','=','i','a','4','G','#']
	print(" ",end="")
	
	i = 0
	while 1:
		if i > 8:
			print("#",end="")
			return	
		if v < t[i]:
			print(c[i],end="")
			return
		i += 1

#Prints out the grid in ascii characters
def printgrid(grid):
	for x in grid:
		for y in x:
			printitem(y)
		print("");

#Randomly returns a value -rng/2 < v < rng/2
def deviate(rng):
	return (random.random() * rng) - (rng/2)

#Diamond phase of the algorithm
def diamond(grid,gridsize,fs,rng):
	fs = int(fs)
	hs = int(fs/2)
	
	x = hs
	y = hs
	while x < gridsize:
		while y < gridsize:
			sum = 0.0
			sum += grid[x-hs][y-hs]
			sum += grid[x+hs][y-hs]
			sum += grid[x-hs][y+hs]
			sum += grid[x+hs][y+hs]
			grid[x][y] = (sum/4.0) + deviate(rng)
			y += fs
		x += fs
		y = hs

#Square phase of the algorithm
def square(grid,gridsize,fs,rng):
	fs = int(fs)
	hs = int(fs/2)
	
	x = 0
	y = hs
	while x < gridsize:
		while y < gridsize:
			sum = 0.0
			items = 0.0
			if x > 0:
				sum += grid[x-hs][y]
				items += 1
			if y > 0:
				sum += grid[x][y-hs]
				items += 1
			if x < gridsize-1:
				sum += grid[x+hs][y]
				items += 1
			if y < gridsize-1:
				sum += grid[x][y+hs]
				items += 1
			
			grid[x][y] = (sum/items) + deviate(rng)
			y += fs
		x += fs
		y = hs
	
	x = hs
	y = 0
	while x < gridsize:
		while y < gridsize:
			sum = 0.0
			items = 0.0
			if x > 0:
				sum += grid[x-hs][y]
				items += 1
			if y > 0:
				sum += grid[x][y-hs]
				items += 1
			if x < gridsize-1:
				sum += grid[x+hs][y]
				items += 1
			if y < gridsize-1:
				sum += grid[x][y+hs]
				items += 1
			
			grid[x][y] = (sum/items) + deviate(rng)
			y += fs
		x += fs
		y = 0

def main():
	#Ensure command line input is valid
	if len(sys.argv) < 2 or len(sys.argv) > 4:
		print("Format: " + sys.argv[0] + " [grid size] [roughness*] [falloff*]")
		print("*: Optional parameter")
		return
	
	gridsize = 0
	try:
		gridsize = int(sys.argv[1])
	except:
		print("Error: Grid size must be an integer")
		return
		
	test = 1
	fail = 1
	while test < gridsize:
		test *= 2
		if test+1 == gridsize:
			fail = 0
	
	if fail:
		print("Error: Grid size must be a power of 2 plus 1")
		return
	
	#Accept the two optional parameters
	if len(sys.argv) > 2:
		try:
			roughness = float(sys.argv[2])
		except:
			print("Error: Roughness must be a number")
			return
	else:
		roughness = 0.5
	
	if len(sys.argv) > 3:
		try:
			falloff = float(sys.argv[3])
		except:
			print("Error: Falloff must be a number")
			return
	else:
		falloff = 0.5
	
	
	#Create grid
	grid = []
	for i in range(gridsize):
		column = []
		for i in range(gridsize):
			column.append(-1)
		grid.append(column)
	
	#Initialize Corners
	grid[0][0] = 4
	grid[gridsize-1][0] = 4
	grid[0][gridsize-1] = 4
	grid[gridsize-1][gridsize-1] = 4
	
	#Run the algorithm
	fs = gridsize-1
	while fs >= 2:
		diamond(grid,gridsize,fs,roughness)
		square(grid,gridsize,fs,roughness)
		fs = int(fs/2)
		roughness = roughness * falloff
	
	printgrid(grid)
	
	
main()





