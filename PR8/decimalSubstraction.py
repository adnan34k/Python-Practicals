def subtract_numstrings(num1,num2):
    if len(num2)>len(num1)or(len(num1)==len(num2) and num2>num1):
        num1,num2 = num2,num1
    num1 =num1[::-1]
    num2 =num2[::-1]
    result =[]
    borrow =0
    for i in range(len(num1)):
        digit1 = int(num1[i])
        digit2 = int(num2[i]) if i<len(num2) else 0
        sub =digit1-digit2-borrow
        if sub<0:
            sub +=10
            borrow=1
        else:
            borrow=0 
        result.append(str(sub))   
    while len(result) > 1 and result[-1]=='0':
        result.pop()
    return ''.join(result[::-1])
result = subtract_numstrings("150","50")
print(result)

