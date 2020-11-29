#All of the question types for music_practice.py are in this file
#There are question bases which have arguments and questions that call those bases with various arguments
#The user selects questions, not bases
#If I add a UI to this, I will probably allow the user to select the arguments themselves

#Uses the functions from music_notation_library.py
from music_notation_library import *
import random

#The main question function all other questions call
#Ask a question and update the score based on if the player got it right
def ask_question(question,answers):
	#Take in user input
	print(question)
	user_answer = input()
	
	#Check the answer
	if user_answer in answers:
		print("Correct!")
		print()
		return True
	else:
		print("Incorrect!")
		print("Expected Answer: " + answers[0])
		print()
		return False

#Asks the player what note is a certain interval above a certain note
#min and max are the smallest/largest intervals to ask about
#notes is the list of notes the test the player on
def base_intervals_1(min,max,notes):
	#Decide the interval to ask about
	interval = int(random.random() * (max-min)) + min
	#Decide the note to ask about
	noteindex = int(random.random() * len(notes))
	note = notes[noteindex]
	
	#Format the question
	question = "What is a " + interval_name(interval) + " above " + notename(note,True) + "?"
	answers = [notename(note + interval,True,False),notename(note + interval,True,True)]
	return ask_question(question,answers)

def intervals_1_easy():
	return base_intervals_1(1,7,[0])
	
def intervals_1_medium():
	return base_intervals_1(1,7,[0,2,4,5,7,9,11])
	
def intervals_1_hard():
	return base_intervals_1(1,7,[0,1,2,3,4,5,6,7,8,9,10,11])

def intervals_1_master():
	return base_intervals_1(1,11,[0,1,2,3,4,5,6,7,8,9,10,11])
	
def intervals_1_grandmaster():
	return base_intervals_1(1,17,[0,1,2,3,4,5,6,7,8,9,10,11])


#Asks the player to tell the notes in a major chord based on root note
#chord is a list of distances from the root note
#notes is the possible root notes to ask about
def base_chords(chordname,chord,notes):
	#Decide the note to ask about
	noteindex = int(random.random() * len(notes))
	note = notes[noteindex]
	
	#Format the question
	question = "Please type out a(n) " + notename(note,True) + " " + chordname + " chord. (Put one space between each note)"
	
	#Build the answers based on the inputted chord
	answer_sharp = ""
	answer_flat = ""
	for dist in chord:
		answer_sharp += notename(note+dist,True,False) + " "
		answer_flat += notename(note+dist,True,True) + " "
	
	#Remove the final space from each answer
	answer_sharp = answer_sharp[:-1]
	answer_flat = answer_flat[:-1]
	
	answers = [answer_sharp,answer_flat]
	return ask_question(question,answers)

def major_chords_white():
	return base_chords("major",[0,4,7],[0,2,4,5,7,9,11])

def major_chords_all():
	return base_chords("major",[0,4,7],[0,1,2,3,4,5,6,7,8,9,10,11])

def minor_chords_white():
	return base_chords("minor",[0,3,7],[0,2,4,5,7,9,11])

def minor_chords_all():
	return base_chords("minor",[0,3,7],[0,1,2,3,4,5,6,7,8,9,10,11])

def diminished_chords_white():
	return base_chords("diminished",[0,3,6],[0,2,4,5,7,9,11])

def diminished_chords_all():
	return base_chords("diminished",[0,3,6],[0,1,2,3,4,5,6,7,8,9,10,11])







