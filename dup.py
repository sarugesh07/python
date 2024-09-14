number=[1,2,1,3,2,3,4,5,6,6]
         
             
for x in range(len(number)):
   for y in range(x+1,len(number)):
       if number[x]==number[y] and x!=y:
           print(number[x])
