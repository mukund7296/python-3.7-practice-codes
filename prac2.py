list = "coffeeshop"

x=len(list)/2
y=int(x)
print(list[:y])
print(list[y:])

import wordninja
n=wordninja.split('bettergood')
m=wordninja.split("coffeeshop")
print(n,m)

list=['hello','coffee','shop','better','good']
mat='coffeeshop'
expected=[]
for i in list:
    if i in mat:
        expected.append(i)
print(expected)
