

def decimal_to_binary(num):
	remainder  = []
	temp = 0
	while(num>0):
		temp = num%2
		num = num//2
		remainder.append(temp)
	remainder.reverse()
	return remainder
	# no need to convert into integers
	#binarynum = 0
	#for i in range(len(remainder)):
	#	binarynum = binarynum*10 + remainder[i]
	#return binarynum
	
def binary_substraction(num1,num2):
	num1 = decimal_to_binary(num1)
	num2 = decimal_to_binary(num2)
	length = max(len(num1),len(num2))
	
	# making both numbers of same length by adding zeros if necessary
	num1 = [0]* (length-len(num1))+num1
	num2 = [0]* (length-len(num2))+num2
	borrow = 0
	result = []
	for i in range(length-1,-1,-1):
		temp = num1[i] - num2[i] - borrow
		if(temp<0):
			borrow = 1
			temp += 2
		else:
			borrow = 0
		result.insert(0,temp) 
	while len(result)>1 and result[0] == 0:
		result.pop(0)
	
	#using above commented code for converting list number to integer
	binarynum = 0
	for i in range(len(result)):
		binarynum = binarynum*10 + result[i]
	return binarynum
	
substraction = binary_substraction(25,11)
print(substraction)
