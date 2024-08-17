def count(string,substring,isbool=False):
   if not substring:
      return 0
   substring_len = len(substring)
   count=0
   if isbool:
      i=0
      while(i<=(len(string)-substring_len)):
         if(string[i:i+substring_len]==substring):
            count = count+1
         i +=1
      return count
   else:
      i=0
      while(i<=(len(string)-substring_len)):
         if(string[i:i+substring_len]==substring):
            count = count+1
            i += substring_len
         else: i=i+1
      return count
   
    
      
print(count('enieeee','eeee'))
