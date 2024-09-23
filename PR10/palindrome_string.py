def ispalindrome(s):
	return s==s[::-1]
	
def fun(arr):
	count=0
	for obj in arr:
		if isinstance(obj,str) and len(obj)%5==3:
			count +=ispalindrome(obj)
		elif isinstance(obj,int):
			obj = repr(obj)
			if len(obj)%5==3:
				count +=ispalindrome(obj)
		elif isinstance(obj,(list,tuple,set)) :
			temp = fun(obj)
			count+=temp
	return count
	
result = fun(["abbbbbba",[[("11222211"),{"aabbbcacbbbaa",11222211}],"aabbbcacbbbaa"]])
print(result)
