# SOS game
import random


def givegriddata(row,col):
	grid = []
	for i in range(col):
		tempdic = {}
		tempdic = tempdic.fromkeys((range(1,col+1)),'')
		grid.append(tempdic)
		
	#now inserting numbers in dictionary
	
	for d in grid:
		for key in d:
			tempnum = str(generateRandom())
			d[key] = tempnum
			
	print(grid)
	return grid
	
def initialize(row=3,col=3):
	grid = givegriddata(row,col)
	for i in range(row):
			print('----'*(col)+'-')
			temprow = '| '+' | '.join(f'{grid[i][j]}' for j in range(1,col+1))+' | '	
			print(f'{temprow}')
	print('----'*(col)+'-')	

def generateRandom():
	return random.randint(1,9)
		
initialize(5,7)

	



