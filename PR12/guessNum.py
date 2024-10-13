import random

def generateRandom():
	return random.randint(1,100)

def playGame():
	randnum = random.randint(1,2000)
	chance = 10
	while(1):
		if chance==0:
			print('chances are over')
			return 0
		num = int(input('Guess the number between 1 to 2000:  '))
		if(num==randnum):
			print('Congratulations you won')
			return 1
		elif(num>(randnum+10)):
			print('too large')
		elif(num>randnum):
			print('a bit large')
		
		elif(num<(randnum+10)):
			print('too small')
		elif(num<randnum):
			print('a bit small')
		chance -=1
	return 0

playGame()
