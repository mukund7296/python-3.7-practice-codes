l = [64, 25, 12, 22, 11, 1,2,64, 25, 12, 22, 11, 1,2,44,3,122, 23, 34]
print(l)
for i in range(len(l)):
   for j in range(i+1,len(l)):
       if l[i]>l[j]:
           l[i],l[j]=l[j],l[i]


print (l)

temp=[]
for i in range(2,11,2):
    temp.append(i**2)
    print(temp)
print(temp)