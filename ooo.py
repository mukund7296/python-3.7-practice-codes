
f=open("crosstab1.csv","r")
data=f.read()
words=data.split()
temp=0
for i in words:
    if i=='drink':
        temp+=1

print(temp)