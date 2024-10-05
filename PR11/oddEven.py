def odd_even_objects(arr):
	oddcount = 0
	evencount= 0
	for obj in arr:
		if isinstance(obj, (list,tuple,set)):
			odd_even_objects(obj)
		oddcount +=isinstance(obj, (int,float)) and obj%2!=0
		evencount +=isinstance(obj, (int,float)) and obj%2==0
		
	return[oddcount,evencount]
	
arr = [1,2,3,4,5,6,7,8,8,9,10,11.234,12.6]
result = odd_even_objects(arr)
print(result)
