
myList=[3,5,9,10,15,18,20,21]
result=[]
for num in myList:
     if num %3 ==0 and num % 5 !=0:
         result.append(num)
print(result)