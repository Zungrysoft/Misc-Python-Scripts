#Basic template for including suspect data

#Define question list
#Items in brackets allow the user to type additional information. Only supports one of these per question.
question_list = [
	["arrest_threat", "We have very damning evidence for your arrest. Would you like to confess now?"],
	["ultragold", "What do you know about UltraGold Tech?"],
	["suspect", "What do you know about |SUSPECT|?"],
]

#Define suspect data
suspect_data = {
	"Haley Derkins": {
		"arrest_threat": "I don't believe you have such evidence as I have not committed any crime.",
		"ultragold": "I work there. Nothing you would be interested in though.",
		"suspect": {
			"default": "Sorry, but I don't know who that is.",
			"Thomas Lord": "He's my next-door neighbor. Very quiet type. The only time I really see him is when he goes out to buy food at the local Target.",
			"Haley Derkins": "I am a software developer at UltraGold Tech and I play the bagpipes!",
		},
	},
	"Thomas Lord": {
		"arrest_threat": "On the advice of my lawyer, I would like to exercise my fifth amendment rights.",
		"ultragold": "On the advice of my lawyer, I would like to exercise my fifth amendment rights.",
		"suspect": {
			"default": "On the advice of my lawyer, I would like to exercise my fifth amendment rights.",
			"Thomas Lord": "Why are you talking to me in the third person?",
		},
	},
}

#Define the default answer for when a suspect doesn't have an answer assigned to that question
default_answer = "I'm sorry, but I really don't know how to answer that."
