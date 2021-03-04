#A library used to make conversions between different formats and do math between notes
#Written by ZungryWare

#notes are numbers measured in distance from C4 (A4 == 440Hz)
#frequencies are numbers measured in Hz

import math

#Pass in a frequency to get the note it is closest to
def frequency_to_note(f):
	middle_c = 261.6255653
	output = 12 * math.log(f/middle_c,2)
	return round(output)
	
#Pass in a note to get its frequency
#Uses equal temperament with A == 440Hz
#Return value is rounded to three decimal places
def note_to_frequency(n):
	middle_c = 261.6255653
	output = middle_c * (2**(n/12))
	return round(output,3)
	
#Pass in a note to get a string representation of that note
#Set flat to true to get accidentals written as flats instead of sharps
def notename(n,no_octave=False,flat=False):
	note_bases_sharp = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
	note_bases_flat = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']
	
	note_base = n % 12
	
	if no_octave:
		note_octave = ""
	else:
		note_octave = str(math.floor(n/12) + 4)
	
	if flat:
		return note_bases_flat[note_base] + note_octave
	return note_bases_sharp[note_base] + note_octave
	
#Prints the string form of a note
def print_note(n,no_octave=False,flat=False):
	print(notename(n,no_octave,flat))

#Pass in an interval (in semitones) and get the name of an interval
#To find the interval between two notes, pass their difference into this function [eg: interval_name(note_1 - note_2)]
#Returns NULL if the difference was too large
def interval_name(i):
	i = abs(i)
	#Values are hard-coded for now
	#I might make an infinitely-expandable system later
	#An infinite system would still need to know the english words for the interval sizes. (Fourth, Seventh, etc.)
	intervals = ["Unison","Minor Second","Major Second","Minor Third","Major Third","Perfect Fourth","Tritone","Perfect Fifth","Minor Sixth","Major Sixth","Minor Seventh","Major Seventh","Octave","Minor Ninth","Major Ninth","Minor Tenth","Major Tenth","Pefect Eleventh","Octave + Tritone","Perfect Twelfth","Minor Thirteenth","Major Thirteenth","Minor Fourteenth","Major Fourteenth","Two Octaves"]
	
	if i >= len(intervals):
		return NULL
	return intervals[i]

#Pass in a guitar string and its fret number and get back a note
def fret_to_note(string,fret):
	strings = [4,-1,-5,-10,-15,-20]
	
	#Make sure the chosen string is an actual string
	if string > len(strings):
		return None
	if string <= 0:
		return None
	
	#Handle the input fret
	if fret == 'o' or fret == 'O':
		fret = 0
	try:
		fret = int(fret)
	except Exception as e:
		return None
	
	return strings[string-1] + fret


