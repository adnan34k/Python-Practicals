# DFA which accept all the strings over {a,b} which ends with 'a'
# output either Accepted or Rejected
	#FA = (E,q0,D,Q,F)
	#alphabet = {a,b}
	#final_state = {q1}
	#text = 
	#state = q0(text)
	
def DFA_endswith_a(text):
	return 'accepted' if q0(text) else 'rejected'
	
def q0(text):
	if len(text) == 0: return False
	if text[0] == 'a' and len(text) == 1:
		return True
	if(text[0]=='a'):
		return q1(text[1:])
	elif text[0] =='b':
		return q0(text[1:])
		
	return False

def q1(text):
	if(len(text)==0): return True
	if text[0]=='a' :
		return q1(text[1:])
	elif text[0]=='b':
		return q0(text[1:])
	return False
	
result = DFA_endswith_a("abbababaaba")
print(result)
		
		

	
	
	
	
