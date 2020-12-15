#A script that lets you enter the names of suspects to interrogate.
#Designed for murder-mystery style investigation games.
#Code by Zungrysoft
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
# *
#End anti-spoiler text
#If you're playing the game, you had better not be reading this! >:|

#Import the suspect data
from data.suspect_data import *
import sys
from colorama import init
init()

#Prints colored text
def print_color(s,c=0):
	#Define the colors
	colors = [
		"\033[37m",
		"\033[31m",
		"\033[32m",
		"\033[36m",
	]
	
	#Bind c within the possible colors
	if c < 0 or c > len(colors):
		c = 0
	
	#Print
	print(colors[c] + s + colors[0])
	

#Pass user input string into here to parse it into a question id
def parse_question_id(q_num):
	try:
		q_num = int(q_num)
	except Exception:
		if Exception == KeyboardInterrupt:
			exit();
		else:
			print_color("Please type an integer number",1);
			return -1
	
	if q_num < 1 or q_num > len(question_list):
		print_color("Please type a valid question number",1);
		return -1
	
	return q_num-1

#Prompts the user to ask a question and returns the question's question code
def ask_question(suspect_name):
	#Print the list of available questions
	print_color("----------------------------------------------------",3);
	i = 1
	for question in question_list:
		print_color(str(i) + ": " + question[1],3)
		i += 1
	
	print_color("----------------------------------------------------",3);
	print_color("Please type the number of the question you wish to ask " + suspect_name + ":",0);
	
	#Get the question code
	question_id = -1
	while(1):
		q_num = input()
		question_id = parse_question_id(q_num)
		if question_id != -1:
			break
	
	#Get question's data from the returned number
	question_code = question_list[question_id][0]
	question_text = question_list[question_id][1]
	
	#Determine if this question needs further prompting
	answer = ""
	if '|' in question_text:
		#Separate the specify part
		split_question = question_text.split('|',2)
		
		#Ask the follow-up question
		print_color("Please specify what |" + split_question[1] + "| you wish to ask about",0);
		specify = input()
		
		#Get the specific answer to this question
		specific_answer = suspect_data.get(suspect_name).get(question_code).get(specify)
		
		#Format the new question and answer text
		question_text = split_question[0] + specify + split_question[2]
		if specific_answer:
			answer = specific_answer
		else:
			answer = suspect_data.get(suspect_name).get(question_code).get("default")
	else:
		answer = suspect_data.get(suspect_name).get(question_code)
	
	#Put in the default answer if one hasn't been found
	if (not answer):
		answer = default_answer
	
	#Print the exchange
	print_color("You: \"" + question_text + "\"",2)
	print_color(suspect_name + ": \"" + answer + "\"",2)

def main():
	#Run the suspect questioning loop
	while (1):
		print_color("Please enter the name of the suspect you wish to interrogate:",0)
		suspect_name = input()
		if (suspect_name.lower() == "exit" or suspect_name.lower() == "quit"):
			exit()
		if (suspect_name in suspect_data):
			ask_question(suspect_name)
		else:
			print_color("That suspect is not known. Check your spelling and try again.",1)

main()





























