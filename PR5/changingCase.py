text = "   ABcDeF JHKL   "
style = 'u'
# c- capitalise
# s - smallcase
# r - reversecase
# u- alter case

   
def iseven(i):
   return i%2 ==0
   
def isodd(i):
   return i%2 !=0
   
   
#def low(c):
   #ans = chr(ord(c) +32)
   #return ans
   
#def up(c):
   #ans = chr(ord(c)-32)
   #return ans
   
   
#to uppercase
def uppercase(text):
   ans = ""
   
   for i in text:
      #check is capital
      if(65<=ord(i) and ord(i)<=90):
         ans += i
         
      # check if small
      if(ord(i) >=97 and ord(i)<=122):
         ans += chr(ord(i)-32)
   return ans


#to lowercase
def lowercase(text):
   ans = ""
   
   for i in text:
      # check if small
      if(ord(i) >=97 and ord(i)<=122):
         ans += i
         
      #check is capital
      if(65<=ord(i) and ord(i)<=90):
         ans += chr(ord(i)+32)
   return ans
 
# reversing case of each character
def reversecase(text):
   ans = ""
   #changing the string to unicode and checking range
   for i in text:
      #from capital to small
      if(65<=ord(i) and ord(i)<=90):
         ans += chr(ord(i)+32)         
         
      #from small to capital       
      elif(97<=ord(i) and ord(i)<=122):
         ans += chr(ord(i)-32)
   return ans
   
#alternatly swap cases      
def ultercase(text):
   ans = text[0]
   if(ord(text[0]) >=97 and ord(text[0])<=122): #first char is lowercase
      for i in range(1,len(text)):
         if(isodd(i)):
            ans +=  chr(ord(text[i])-32) if(97<=ord(text[i])<=122)else text[i]
         elif(iseven(i)):
            ans += chr(ord(text[i])+32) if(65<=ord(text[i])<=90)else text[i]
   elif(ord(text[0])>=65 and ord(text[0])<=90): #first char is uppercase
      for i in range(1,len(text)):
         if(isodd(i)):
            ans += chr(ord(text[i])+32) if(65<=ord(text[i])<=90)else text[i]
         elif(iseven(i)):
            ans += chr(ord(text[i])-32) if (97<=ord(text[i])<=122)else text[i]
   return ans


def changecase(text,style):
   if not text:
      print('invalid text')
      exit()
   if(style=='c' or style=='C'):
      ans = uppercase(text)
      print(ans)
      
   elif(style=='s' or style=='S'):
      ans = lowercase(text)
      print(ans)
      
   elif(style=='r' or style=='R'):
      ans = reversecase(text)
      print(ans)
      
   elif(style=='u' or style=='U'):
      ans = ultercase(text)
      print(ans)
      
   else:
      print("please enter valid style")
      exit()
      
text = text.strip()
changecase(text,style)
