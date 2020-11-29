#A program written for myself to practice various music subjects
#I integrated it into my schedule so I would practice at it once a day
#I continue to add new question sets as time goes on

#Uses the functions from music_notation_library.py
from music_notation_library import *
from datetime import datetime
import random

#Global variable to track score
score = 0

#Ask a question and update the score based on if the player got it right
def ask_question(question,answers):
	global score
	
	#Take in user input
	user_answer = input(question)
	
	#Check the answer
	if user_answer in answers:
		score += 1
		print("Correct!")
	else:
		print("Incorrect!")
		print("Expected Answer: " + answers[0])

#Asks the player what note is a certain interval above a certain note
#min and max are the smallest/largest intervals to ask about
def q_intervals_1(min,max):
	#Decide the interval to ask about
	interval = int(random.random() * (max-min)) + min
	#Decide the note to ask about
	note = int(random.random() * 12)
	
	#Format the question
	question = "What is a " + interval_name(interval) + " above " + notename(note) + "?  "
	answers = [notename(note + interval,False),notename(note + interval,True)]
	ask_question(question,answers)

#Goes through all of the questions and picks one proportional to its weight
def pick_question(question_set):
	#Figure out the sum total of weights
	sum = 0
	for item in question_set:
		sum += item[1]
	
	#Pick an item based on the weights
	choice = int(random.random() * sum)
	
	#Determine which item to choose based on the chosen weight
	for item in question_set:
		choice -= item[1]
		if choice <= 0:
			return item[0]
	
	#Default selection
	return question_set[0][0]

def main():
	start_time = datetime.now()
	question_count = 3
	filename = 'example_question_set.txt'
	
	#Read in the question set from the chosen file
	question_set = []
	file = open(filename, 'r')
	line_num = 0
	for line in file:
		#Ensure line isn't a comment line and there's actual text on the line
		if len(line) > 1 and line[0] != "#":
			items = line.split(" ")
			#Ensure proper formatting
			if len(items) == 2:
				items[1] = int(items[1])
				question_set.append(items)
			else:
				print("Error reading file")
				print("Line " + str(line_num) + " is formatted incorrectly")
				continue
		line_num += 1
	
	#Ask the questions
	for i in range(question_count):
		#Pick a question
		choice = pick_question(question_set)
		
		try:
			#Call the corresponding function based on the chosen question
			#And yes, I know this is a dangerous way to do things :P
			#But this is faster than making an array of valid functions to call
			globals()[choice](1,12)
		except(e):
			print("Error: Invalid question type " + choice)
			
	
	#Calculate time spent on problems
	timediff = (datetime.now() - start_time).total_seconds()
	
	#Print the final results
	print()
	print("Your score is " + str(score) + "/" + str(question_count))
	print("Your time is " + str(timediff) + " seconds")
	

main()





