import time
def ispalindrome2(s):
	return s==s[::-1]
	
def ispalindrome1(s):
	l=0;r=len(s)-1
	while(l<r):
		if(s[l]!=s[r]):
			return False
		l+=1
		r-=1
	return True

	
def fun2(arr):
	count=0
	for obj in arr:
		if isinstance(obj,str) and len(obj)%5==3:
			count +=ispalindrome2(obj)
		elif isinstance(obj,int):
			obj = str(obj)
			if len(obj)%5==3:
				count +=ispalindrome2(obj)
		elif isinstance(obj,(list,tuple,set)) :
			temp = fun2(obj)
			count+=temp
	return count
	
def fun1(arr):
	count=0
	for obj in arr:
		if isinstance(obj,str) and len(obj)%5==3:
			if ispalindrome1(obj):
				count +=1
		elif isinstance(obj,int):
			obj = repr(obj)
			if len(obj)%5==3:
				if ispalindrome1(obj):
					count +=1
		elif isinstance(obj,(list,tuple,set)) :
			temp = fun1(obj)
			count+=temp
	return count


def fun3(arr):
	count=0
	for obj in arr:
		if isinstance(obj,(list,tuple,set)) :
			count +=fun3(obj)
		elif type(obj)==int:
			obj = str(obj)
			
		count+= type(obj)==str and len(obj)%5==3 and obj==obj[::-1]
			

			
	return count

avgtime1 =[]
avgtime2 = []
avgtime3 = []

for i in range(100):
	t1 = time.time()
	result3 = fun1(["abbbbbba",[[("11222211"),{"aabbbcacbbbaa",11222211}],"aabbbcacbbbaa"]])
	t2 = time.time()
	avgtime3.append(t2-t1)
avgtime3 = sum(avgtime3)/100

for i in range(100):
	t1 = time.time()
	result1 = fun1(["abbbbbba",[[("11222211"),{"aabbbcacbbbaa",11222211}],"aabbbcacbbbaa"]])
	t2 = time.time()
	avgtime1.append(t2-t1)
avgtime1 = sum(avgtime1)/100
for i in range(100):
	t3 = time.time()
	result2 = fun2(["abbbbbba",[[("11222211"),{"aabbbcacbbbaa",11222211}],"aabbbcacbbbaa"]])
	t4 = time.time()
	avgtime2.append(t4-t3)
avgtime2 = sum(avgtime2)/100

print(f"performance of my method: {avgtime1}")
print(f"performance of sir's method: {avgtime2}")
print(f"performance of 3rd method: {avgtime3}")
chance = max(avgtime1,avgtime2,avgtime3)
print(f"more time is {chance}")
print(result1)
print(result2)
print(result3)


