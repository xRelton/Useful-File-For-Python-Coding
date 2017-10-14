def userInput(content, answers, printNums):
	while(True):
		if(printNums == True):
			output = input(content+" ("+("{}/"*len(answers)).format(*answers)[:-1]+") ").lower()
		else:
			output = input(content+" ").lower()
		if(output not in answers):
			print("Please input a valid answer")
		else:
			return(output)

def inputInt(content):
	while(True):
		output = input(content)
		try:
			int(output)
			return int(output)
		except ValueError:
			print("Please input an integer")

def inputString(content):
	while(True):
		output = input(content)
		try:
			str(output)
			return output
		except ValueError:
			print("Please input a string")

def menu(options):
	print("You have {} options:".format(len(options)))
	numbers = []
	for i in range(0,len(options)):
		numbers.insert(i,str(i+1))
		print("\n{}. {}".format(i+1,options[i]))
	menuOption = int(userInput("\nInput one of the previous numbers:",numbers,False))
	return menuOption