def check_validity(s: str):
# [], {}, <>, ()
# string is given - "[](){}<>"
# "[{()}]"
# empty string is invalid
	if not s: return 0
	
	brackets = {')':'(', ']':'[', '}':'{', '>':'<'}
	stack = []
	for char in s:
		if char in "[{(<":
			stack.append(char)
		elif char in "]})>":
			if not stack or stack.pop()!=brackets[char]:	
				return 0
		else:
			return 0
	return 0 if not stack else 0
					
def get_count(arr):
	valid = 0
	invalid = 0
	for i in arr:
		if isinstance(i,str):
			if check_validity(i)==1:
				valid +=1
			else:
				invalid +=1
	return (valid,invalid)
	
arr = [[1,2,3],(1,2,3),{1,2,3},"","[+]","+{}","(1)",")(}{][",("()"),[45,("()")]]
print(get_count(arr))
