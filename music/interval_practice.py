# Modified version of music_practice.py specifically for practicing intervals
# Written by ZungryWare

# Uses the functions from music_notation_library.py
from music_notation_library import *
# Import all of the music practice questions for use
from music_practice_questions import *
from datetime import datetime
import random
import sys

# Ask the question
def pick_question(note, interval):
	min = 1
	max = 11
	is_flat = random.random() < 0.5

	# Decide the interval to ask about
	if (interval == -1):
		interval = int(random.random() * (max-min)) + min
	
	# Decide the note to ask about
	if (note == -1):
		note = int(random.random() * 12)
		
	print(interval)
	print(note)
	
	# Format the question
	question = f"What is a {interval_name(interval)} above {notename(note,True,is_flat)}?"
	answers = [
		notename(note + interval,True,False),
		notename(note + interval,True,True),
	]
	return ask_question(question,answers)

def main():
	# Ensure command line input is valid
	if len(sys.argv) != 2:
		print("Format: " + sys.argv[0] + " [question count]")
		return
	
	# Parse question count
	try:
		question_count = int(sys.argv[1])
	except:
		print("Error: [question count] must be an integer number")
		return
	
	
	# Stores the start time of the program for tracking the player's time
	start_time = datetime.now()
	# The number of correct questions the player has gotten
	score = 0
	
	# Determine what we're asking today
	chosen_note = -1
	chosen_interval = -1
	if random.random() < 0.5:
		chosen_interval = int(random.random() * (max-min)) + min
	else:
		chosen_note = int(random.random() * 12)
	
	# Ask the questions
	for i in range(question_count):	
		correct_answer = pick_question(chosen_note, chosen_interval)
		if correct_answer:
			score += 1
	
	#Calculate time spent on problems
	timediff = (datetime.now() - start_time).total_seconds()
	timediff_seconds = round(timediff%60,3)
	timediff_minutes = int(timediff/60)
	
	#Print the final results
	print()
	percentage = score/question_count*100
	print(f"Your score is {str(score)}/{str(question_count)} ({str(percentage)[:5]}%)")
	
	if timediff_minutes == 0:
		print(f"Your time is {str(timediff_seconds)} seconds")
	else:
		print(f"Your time is {str(timediff_minutes)} minutes and {str(timediff_seconds)} seconds")

main()
