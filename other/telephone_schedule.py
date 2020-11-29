#Telephone Schedule.py
#This system makes a telephone game schedule such that each participant is scheduled for one and only one song each round, is not scheduled for more than one song on any round, and never gets scheduled for the same song twice
#Written by ZungryWare

import random

#Prints one entry in the table with space padding
def printentry(text,columnwidth,includebar=True):
	if includebar:
		print("|",end="")
	print(text,end="")
	pad = columnwidth - len(text)
	for i in range(pad):
		print(" ",end="")

def main():
	#Accept names
	print("Please enter all participant names separated by spaces")
	readin1 = input()
	
	#Handle input
	names = readin1.split(' ')
	namecount = len(names)
	
	#Error Handling
	if (namecount < 2 or namecount > 99):
		print("Error: Number of names must be between 2 and 99")
		return
	
	#Determine the width of the columns by the longest name
	columnwidth = 7
	for i in names:
		if len(i) > columnwidth:
			columnwidth = len(i)
			
	#Print the header
	print("        ",end="")
	count = 1
	for i in names:
		printentry("Song " + str(count),columnwidth)
		count += 1
	print()
	
	#Print the divider
	divcount = 8 + (namecount * (1 + columnwidth))
	for i in range(divcount):
		print("-",end="")
	print()
	
	#Create an empty table
	tablesize = 65
	table = []
	count = 0
	for i in range(namecount):
		row = []
		for i in range(namecount):
			row.append("*Empty*")
			count += 1
		table.append(row)
	
	#Fill out the table with the starting values
	count = 0
	for i in range(len(table)):
		for j in range(len(table[0])):
			table[i][j] = names[count]
			count = (count + 1) % namecount
		count = (count + 1) % namecount
	
	#Randomly shuffle the rows around
	for i in range(namecount * 5):
		r1 = int(random.random() * namecount)
		r2 = int(random.random() * namecount)
		r1save = table[r1]
		r2save = table[r2]
		table[r1] = r2save
		table[r2] = r1save
	
	#Print the table
	count = 1
	for row in table:
		printentry("Round " + str(count),8,False)
		count += 1
		for item in row:
			printentry(item,columnwidth)
		print()
	
main()



