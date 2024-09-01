def romantodecimal(roman):
	symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
	total = 0
	prev_value = 0
	for char in reversed(roman):
		value = symbols[char]
		if value<prev_value:
			total -=value
		else:
			total +=value
		prev_value =value    
	return total

def fordecimal(symbols, num):
	roman = ''
	for i in sorted(symbols.keys(),reverse=True):
		while num >=i:
			roman += symbols[i]
			num -= i
	return roman

def base(text,textbase,outputbase):
	if textbase in ["roman","r","R"]:
		decimalval = romantodecimal(text)
	else:
		decimalval = int(text, textbase)   
	if outputbase == 10:
		return str(decimalval)
	if outputbase in ["roman","r","R"]:
		symbols = {1:'I',4:'IV',5:'V',9:'IX',10:'X',40:'XL',50:'L',90:'XC',100:'C',400:'CD',500:'D',900:'CM',1000:'M'}
		return fordecimal(symbols,decimalval)
 
	result = ""
	while decimalval >0:
		remainder = decimalval % outputbase
		if remainder <10:
			result = str(remainder)+result
		else:
			result = chr(ord('A')+remainder-10)+result
		decimalval //= outputbase
	return result or "0"

print(base("II","roman",2))  
print(base("1100",2,10))    
print(base("C",16,10))  
print(base("12",8,16)) 
print(base("12",10,"R"))   
print(base("FC",16,"r"))  
print(base("X","roman",10))

