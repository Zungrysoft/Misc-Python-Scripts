# A library used to make conversions between different formats and do math between notes
# Written by ZungryWare

# notes are MIDI numbers
# frequencies are numbers measured in Hz

import math

# Pass in a frequency to get the note it is closest to
def frequency_to_note(f):
	middle_c = 261.6255653
	output = 12 * math.log(f/middle_c,2)
	return round(output)
	
# Pass in a note to get its frequency
# Uses equal temperament with A == 440Hz
# Return value is rounded to three decimal places
def note_to_frequency(n):
	middle_c = 261.6255653
	output = middle_c * (2**(n/12))
	return round(output,3)
	
# Pass in a note to get a string representation of that note
# Set flat to true to get accidentals written as flats instead of sharps
def get_notename(n,no_octave=False,flat=False):
	note_bases_sharp = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
	note_bases_flat = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']
	
	note_base = n % 12
	
	if no_octave:
		note_octave = ""
	else:
		note_octave = str(math.floor(n/12) - 2)
	
	if flat:
		return note_bases_flat[note_base] + note_octave
	return note_bases_sharp[note_base] + note_octave
	
# Prints the string form of a note
def print_note(n,no_octave=False,flat=False):
	print(get_notename(n,no_octave,flat))

# Pass in an interval (in semitones) and get the name of an interval
# To find the interval between two notes, pass their difference into this function [eg: interval_name(note_1 - note_2)]
# Returns NULL if the difference was too large
def interval_name(i):
	i = abs(i)
	# Values are hard-coded for now
	# I might make an infinitely-expandable system later
	# An infinite system would still need to know the english words for the interval sizes. (Fourth, Seventh, etc.)
	intervals = ["Unison","Minor Second","Major Second","Minor Third","Major Third","Perfect Fourth","Tritone","Perfect Fifth","Minor Sixth","Major Sixth","Minor Seventh","Major Seventh","Octave","Minor Ninth","Major Ninth","Minor Tenth","Major Tenth","Pefect Eleventh","Octave + Tritone","Perfect Twelfth","Minor Thirteenth","Major Thirteenth","Minor Fourteenth","Major Fourteenth","Two Octaves"]
	
	if i >= len(intervals):
		return None
	return intervals[i]


# Pass in a guitar string and its fret number and get back a note
# Assumes standard tuning
def fret_to_note(string,fret):
	strings = [4,-1,-5,-10,-15,-20]
	
	# Make sure the chosen string is an actual string
	if string > len(strings):
		return None
	if string <= 0:
		return None
	
	# Handle the input fret
	if fret == 'o' or fret == 'O':
		fret = 0
	try:
		fret = int(fret)
	except Exception as e:
		return None
	
	return strings[string-1] + fret

# Pass in a note to get which staff line or gap it should sit on
# Staff lines start at C0
def get_staff_number(note, key_signature=0):
	note_numbers = {
		'C': 0,
		'D': 1,
		'E': 2,
		'F': 3,
		'G': 4,
		'A': 5,
		'B': 6,
	}
	
	notename = get_notename(note, False, key_signature < 0)
	octave_number = int(notename[-1])
	note_number = note_numbers[notename[0]]

	# Flats
	time_signature_default = "natural"
	if key_signature < 0:
		if notename[0] == 'B' and key_signature <= -1:
			time_signature_default = "flat"
		elif notename[0] == 'E' and key_signature <= -2:
			time_signature_default = "flat"
		elif notename[0] == 'A' and key_signature <= -3:
			time_signature_default = "flat"
		elif notename[0] == 'D' and key_signature <= -4:
			time_signature_default = "flat"
		elif notename[0] == 'G' and key_signature <= -5:
			time_signature_default = "flat"
	# Sharps
	else:
		if notename[0] == 'F' and key_signature >= 1:
			time_signature_default = "sharp"
		elif notename[0] == 'C' and key_signature >= 2:
			time_signature_default = "sharp"
		elif notename[0] == 'G' and key_signature >= 3:
			time_signature_default = "sharp"
		elif notename[0] == 'D' and key_signature >= 4:
			time_signature_default = "sharp"
		elif notename[0] == 'A' and key_signature >= 5:
			time_signature_default = "sharp"
	
	note_symbol = ""
	if ("#" not in notename and "b" not in notename) and time_signature_default != "natural":
		note_symbol = "♮"
	elif ('#' in notename) and time_signature_default != "sharp":
		note_symbol = "#"
	elif ('b' in notename) and time_signature_default != "flat":
		note_symbol = "b"

	return note_number + (octave_number * 7), note_symbol

def generate_note_on_staff(note, key_signature=0, clef="auto"):
	ret = ""

	if clef != "treble" and clef != "bass":
		clef = "treble" if note >= 72 else "bass"

	if clef == "treble":
		clef_staff_number = 35
		clef_text1 = "Treble"
		clef_text2 = "Clef  "
	else:
		clef_staff_number = 23
		clef_text1 = "Bass  "
		clef_text2 = "Clef  "

	note_staff_number, note_symbol = get_staff_number(note, key_signature=key_signature)

	for i in range(23):
		staff_number = clef_staff_number + 10 - i
		long_line = i % 2 == 1 and i >= 7 and i <= 15
		short_line = i % 2 == 1

		if i == 9:
			ret += clef_text1
		elif i == 10:
			ret += clef_text2
		else:
			for k in range(6):
				if i == (5 if k % 2 == 0 else 6) and 6 - k <= abs(key_signature):
					ret += '#' if key_signature >= 0 else 'b'
				else:
					ret += ' '
		
		ret += ' '

		for j in range(17):
			if j == 7 and staff_number == note_staff_number:
				ret += '('
			elif j == 8 and staff_number == note_staff_number:
				ret += ')'
			elif j == 9 and staff_number == note_staff_number and note_symbol != "":
				ret += note_symbol
			elif long_line:
				ret += "-"
			elif short_line and j >= 6 and j <= 10 and ((staff_number > clef_staff_number and note_staff_number >= staff_number) or (staff_number < clef_staff_number and note_staff_number <= staff_number)):
				ret += "-"
			else:
				ret += " "
		
		ret += "\n"
	
	return ret
