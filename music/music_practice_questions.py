# All of the question types for music_practice.py are in this file
# There are question bases which have arguments and questions that call those bases with various arguments
#The user selects questions, not bases
# If I add a UI to this, I will probably allow the user to select the arguments themselves
# Written by ZungryWare

# Uses the functions from music_notation_library.py
from music_notation_library import *
import random

# The main question function all other questions call
# Ask a question and update the score based on if the player got it right
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

# Asks the player what note is a certain interval above a certain note
# min and max are the smallest/largest intervals to ask about
# notes is the list of notes the test the player on
def base_intervals_1(min,max,notes):
	# Decide the interval to ask about
	interval = int(random.random() * (max-min)) + min
	# Decide the note to ask about
	noteindex = int(random.random() * len(notes))
	note = notes[noteindex]
	
	# Format the question
	question = "What is a " + interval_name(interval) + " above " + get_notename(note,True) + "?"
	answers = [get_notename(note + interval,True,False),get_notename(note + interval,True,True)]
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


# Asks the player to tell the notes in a major chord based on root note
# chord is a list of distances from the root note
# notes is the possible root notes to ask about
def base_chords(chord_name,chord,notes):
	# Decide the note to ask about
	noteindex = int(random.random() * len(notes))
	note = notes[noteindex]
	
	# Format the question
	question = "Please type out a(n) " + get_notename(note,True) + " " + chord_name + " chord. (Put one space between each note)"
	
	# Build the answers based on the inputted chord
	answer_sharp = ""
	answer_flat = ""
	for dist in chord:
		answer_sharp += get_notename(note+dist,True,False) + " "
		answer_flat += get_notename(note+dist,True,True) + " "
	
	# Remove the final space from each answer
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

# Player is given a key signature and must determine what key it is in
# scale_name is the name of the scale the player must identify the key signature for
# offset is the amount of semitones the root is offset from C
def base_key_signature(scale_name,offset):
	signatures = ["n","#","##","###","####","#####","bbbbbb","bbbbb","bbbb","bbb","bb","b"];
	choice = int(random.random() * 12)
	
	# Format the question
	question = "What is the " + scale_name + " key for the key signature " + signatures[choice] + "?"
	answers = [
		get_notename(offset + (choice*7),True,True),
		get_notename(offset + (choice*7),True,False)
	]
	return ask_question(question,answers)
	
def key_signature_major():
	return base_key_signature("MAJOR",0)

def key_signature_minor():
	return base_key_signature("MINOR",-3)

def key_signature_modes():
	choice = int(random.random() * 7)
	if choice == 0:
		return base_key_signature("LYDIAN",5)
	elif choice == 1:
		return base_key_signature("IONIAN",0)
	elif choice == 2:
		return base_key_signature("MIXOLYDIAN",-5)
	elif choice == 3:
		return base_key_signature("DORIAN",2)
	elif choice == 4:
		return base_key_signature("AEOLIAN",-3)
	elif choice == 5:
		return base_key_signature("PHRYGIAN",4)
	else:
		return base_key_signature("LOCRIAN",-1)

# Player is given two notes and must determine how many semitones note B is above note A.
def note_distance():
	# Determine the two notes
	note = int(random.random() * 12)
	distance = int(random.random() * 11) + 1
	
	# Format the question
	question = "How many semitones apart are " + get_notename(note,True) + " and " + get_notename(note+distance,True) + "?"
	answers = [str(distance),str(abs(distance-12)),str(distance-12)]
	return ask_question(question,answers)

# Player is given a visual representation of the note on a music staff and must say
# What note it is.
def base_sight_reading(note, key_signature=0, clef="auto"):
	question = "What note is this?\n\n" + generate_note_on_staff(note, key_signature, clef)
	answers = [get_notename(note, True, False), get_notename(note, True, True)]
	return ask_question(question, answers)

def sight_reading_easy():
	# Just white notes in the treble clef
	note_options = [74, 76, 77, 79, 81, 83, 84, 86, 88, 89, 91]
	note = random.choice(note_options)
	return base_sight_reading(note, 0, "treble")

def sight_reading_medium():
	# White and black notes in the treble clef
	note = random.randrange(74, 91 + 1)
	return base_sight_reading(note, 0, "treble")

def sight_reading_hard():
	if random.random() < 0.5:
		# Notes that go farther out
		note = random.randrange(67, 98 + 1)
		return base_sight_reading(note, 0, "treble")
	
	# Key signatures with up to 3 sharps or flats
	note = random.randrange(74, 91 + 1)
	key_signature = random.randrange(-3, 3 + 1)
	return base_sight_reading(note, key_signature, "treble")

def sight_reading_master():
	r = random.random()

	if r < 0.2:
		# Notes that go even farther out on treble clef
		note = random.randrange(64, 101 + 1)
		return base_sight_reading(note, 0, "treble")

	if r < 0.6:
		# Key signatures with up to 5 sharps or flats
		note = random.randrange(67, 98 + 1)
		key_signature = random.randrange(-5, 5 + 1)
		return base_sight_reading(note, 0, "treble")
	
	# Bass clef
	note = random.randrange(53, 71 + 1)
	return base_sight_reading(note, key_signature, "bass")

def sight_reading_grandmaster():
	r = random.random()

	if r < 0.33:
		# Notes that go even farther out on treble clef with up to 5 sharps/flats in key signature
		note = random.randrange(64, 101 + 1)
		key_signature = random.randrange(-5, 5 + 1)
		return base_sight_reading(note, 0, "treble")

	if r < 0.66:
		# Notes that go all across both clefs with full range
		note = random.randrange(43, 101 + 1)
		return base_sight_reading(note, 0, "auto")
	
	# Both clefs with key signatures with up to 3 sharps or flats
	note = random.randrange(53, 91 + 1)
	key_signature = random.randrange(-3, 3 + 1)
	return base_sight_reading(note, key_signature, "auto")

def sight_reading_ultragrandmaster():
	# Everything
	note = random.randrange(43, 101 + 1)
	key_signature = random.randrange(-5, 5 + 1)
	return base_sight_reading(note, key_signature, "auto")
