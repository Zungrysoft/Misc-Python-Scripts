#A script written to convert guitar tab fret numbers to chords

from music_notation_library import *

def main():
	print("Input the frets separated by spaces")
	chord = input()
	frets = chord.split(" ")
	
	string = 6
	for fret in frets:
		note = fret_to_note(string, fret)
		if type(note) == int:
			print(get_notename(note))
		string -= 1
		

main()
