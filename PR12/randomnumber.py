import random

def generateRandom():
	return random.randint(1,100)
	
def startGame():
	randnum = generateRandom()
	while(1):
		num = int(input("enter an integer between range 1 to 100: "))
		if(num==randnum):
			print('correct')
			return 1
		if(num>randnum):
			print('too large')
		elif(num<randnum):
			print('too small')
	return 0

startGame()

		


