def slice(st,list1=None):
    if list1 is None:
        list1 = [0,len(st)-1,1]

    start, end, step = list1

    if step ==0:
        return "Value error: slice step cannot be 0"
    
    if(type(st)==str):
        result = ""
        if step>0:
            if start>end:
                return result
            for i in range(start,end+1,step):
                if 0<=i<len(st):
                    result += st[i]
        elif step<0:
            if start< end:
                return result
            for i in range(start,end-1,step):
                if 0<=i<len(st):
                    result += st[i]
        return result

    elif (type(st)==list) :
        result = []
        if step>0:
            if start>end:
                return result
            for i in range(start,end+1,step):
                if 0<=i<len(st):
                    result.append(st[i])
        elif step<0:
            if start<end:
                return result
            for i in range(start,end-1,step):
                if 0<=i<len(st):
                    result.append(st[i])
        return result

    else:
        return "not valid datatype"

list1 = [26,1,-1]
arr = [1,2,3]
st = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = slice(arr,list1)
print(ans)

