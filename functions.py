def userInput(text, answers):
	while(True):
		condition = input(text+" ("+((("{}")+"/")*len(answers)).format(*answers)[:-1]+") ").lower()
		if(condition not in answers):
			print("Please input a valid answer")
		else:
			return(condition)
