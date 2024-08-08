
def finalMethod(num):
    spaces = num*2+2
    nextspace = 3
    for i in range(num-1):
        if(i==0):
            print(' '*spaces+'+'+' '*spaces)
            spaces = spaces-2
        if(i == num-2):
            print(' '*spaces+'+'+' '*(nextspace//2)+'*'+' '*(nextspace//2)+'+')
            spaces = spaces-2
            nextspace += 4
        else:
            print(' '*spaces+'+'+' '*nextspace+'+') 
            spaces = spaces-2
            nextspace += 4
    
def belowpattern(num):
    spaces = 3
    nextspaces = (num*4)-2
    for i in range(num):
        if(i==num-1):
           spaces +=1
           print(' '*spaces+'-'+' '*nextspaces)
           
           nextspaces =nextspaces - 4
        else:
           print(' '*spaces+'-'+' '*nextspaces+'-')
           spaces +=2
           nextspaces =nextspaces - 4
	
	
	
	
def pattern(num):
    if(num<1):
        print('please enter a positive number')
    if (num !=int(num)):
        print('please enter an integer value')
    else:
        finalMethod(num)
        belowpattern(num)

num = int(input('enter number\n'))
pattern(num)
