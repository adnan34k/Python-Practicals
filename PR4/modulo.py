def modulo(num1,num2):
	ans = 0
	if(num2 ==0):
		print('invalid inputs')
	elif(num1==0):
		print(0)
	elif(num1==num2):
		print(0)
		
	elif(num2>0 and num1>0 ):
		for i in range(num1):
			ans = i*num2
			if(ans > num1):
				ans = num2*(i-1)
				ans = num1-ans
				print(ans)
				break
	elif(num2<0 and num1<0):
		num2 = -num2
		num1 = -num1
		for i in range(num1):
			ans = i*num2
			if(ans > num1):
				ans = num2*(i-1)
				ans = num1-ans
				print(-ans)
				break
	elif((num1<0 and num2>0)):
		num1 = -num1
		for i in range(num1):
			ans = i*num2
			if(ans > num1):
				ans = ans-num1
				print(-ans)
				break
	elif((num1>0 and num2<0)):
		num2 = -num2
		for i in range(num1):
			ans = i*num2
			if(ans > num1):
				ans = ans - num1
				print(-ans)
				break
modulo(40,-7)
