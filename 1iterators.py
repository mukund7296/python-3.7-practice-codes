

list1=[1,2,3,4,5,6,7,8,9]

for i in list1:
    print(i)

s="Python tutorial"

for char in s:
    print(char)

d={"a":1,"b":2,"c":4}
for i in d.items():
    print(i)

list1=[1,2,3,4,5,6,7,8,9]
c=iter(list1)
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())

