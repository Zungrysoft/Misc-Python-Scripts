#A program written for myself to practice various music subjects
#I integrated it into my schedule so I would practice at it once a day
#I continue to add new question sets as time goes on
#Written by ZungryWare

#Uses the functions from music_notation_library.py
from music_notation_library import *
#Import all of the music practice questions for use
import music_practice_questions
from datetime import datetime
import random
import sys

#Goes through all of the questions and picks one proportional to its weight
def pick_question(question_set):
	#Figure out the sum total of weights
	sum = 0
	for item in question_set:
		sum += int(item[1])
	
	#Pick an item based on the weights
	choice = int(random.random() * sum)
	
	#Determine which item to choose based on the chosen weight
	for item in question_set:
		choice -= int(item[1])
		if choice < 0:
			return item[0]
	
	#Default selection
	return question_set[0][0]

def main():
	#Ensure command line input is valid
	if len(sys.argv) < 2 or len(sys.argv) > 3:
		print("Format: " + sys.argv[0] + " [question count] [question set file*]")
		print("*: Optional parameter")
		return
	
	#Determine filename value
	filename = "example_question_set.txt"
	if len(sys.argv) > 2:
		filename = sys.argv[2]
	
	#Parse question count
	try:
		question_count = int(sys.argv[1])
	except:
		print("Error: [question count] must be an integer number")
		return
	
	
	#Stores the start time of the program for tracking the player's time
	start_time = datetime.now()
	#The number of correct questions the player has gotten
	score = 0
	
	#Read in the question set from the chosen file
	question_set = []
	file = open(filename, 'r')
	line_num = 0
	for line in file:
		#Ensure line isn't a comment line and there's actual text on the line
		if len(line) > 3 and line[0] != "#":
			question_set.append(line.split(" "))
		line_num += 1
	
	#Ask the questions
	for i in range(question_count):
		#Pick a question
		choice = pick_question(question_set)
		
		try:
			#Call the corresponding function based on the chosen question
			#And yes, I know this is a dangerous way to do things :P
			#But this is faster than making an array of valid functions to call
			correct_answer = getattr(music_practice_questions, choice)()
			if correct_answer:
				score += 1
		except KeyboardInterrupt:
			sys.exit(0)
		except:
			print("Error: Invalid question type " + choice)
	
	#Calculate time spent on problems
	timediff = (datetime.now() - start_time).total_seconds()
	timediff_seconds = round(timediff%60,3)
	timediff_minutes = int(timediff/60)
	
	#Print the final results
	print()
	print("Your score is " + str(score) + "/" + str(question_count))
	
	if timediff_minutes == 0:
		print("Your time is " + str(timediff_seconds) + " seconds")
	else:
		print("Your time is " + str(timediff_minutes) + " minutes and " + str(timediff_seconds) + " seconds")

main()





