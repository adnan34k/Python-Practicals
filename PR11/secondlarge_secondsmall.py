# we have to find second large number and second small number from a list objects
# objects can be int ,string, set, dict, list, tuple
# if list or tuple or set recursion
# in case of string ignore
# in case of dictionary check all values and keys also and second largest and second smallest among all of them

temp = []
def get_SL_SS(arr):
	SL, SS = 0,0
	for obj in arr:
		if isinstance(obj, str):
			continue
		elif isinstance(obj, (list,tuple,set)):
			get_SL_SS(obj)
		elif isinstance(obj,int):
			temp.append(obj)
		elif isinstance(obj, dict):
			valuesArr = []
			valuesArr = list(obj.values())
			keysArr = []
			keysArr = list(obj.keys())
			get_SL_SS(valuesArr)
			get_SL_SS(keysArr)
		elif isinstance(obj, complex):
			val = obj.real
			temp.append(val)
	temp.sort()
	if len(temp)==1: return temp[0]
	SL = temp[len(temp)-2]
	SS = temp[1]
	return [SS,SL]
arr = [1,2,3,"23","sds",[25,350,450],(23,56,"fg"),{1000,999},{'a':1555},{3434:33434},919191+56j]
ans = get_SL_SS(arr)
print(ans)
		
			
