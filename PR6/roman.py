# program to convert a number into roman number
#def rom(String, base)

def fordecimal(symbols,st):
	num = int(st)
	roman = ''
	for i in sorted(symbols.keys(),reverse=True):
		while num>=i:
			roman += symbols[i]
			num -=i
	return roman
	
	
def foroctal(symbols,st):
	num = int(st,8)
	return fordecimal(symbols,str(num))
	
def forbinary(symbols,st):
	num = int(st,2)
	return fordecimal(symbols,str(num))
	
def forhexadecimal(symbols,st):
	num = int(st,16)
	return fordecimal(symbols,str(num))
	
def rom(st,base):
	symbols = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
	if(base==10): return fordecimal(symbols,st)
	elif(base==8): return foroctal(symbols,st)
	elif(base==2): return forbinary(symbols,st)
	elif(base==16): return forhexadecimal(symbols,st)
		
print(rom("12",10))	
print(rom("12",8))	
print(rom("11",2))	
print(rom("F",16))	

