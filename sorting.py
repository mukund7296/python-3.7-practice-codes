def minmax(n):
    a=sorted(n)
    mini=0
    max=0
    d=[]
    for i in a:
        if i>=0:
            d.append(i)
    ll=len(d)
    for i in range(ll-1):
        max+=n[i]
        mini+=n[i+1]
    print(mini,max)

#  Driver Code
arr=[10, 9, 8, 7, 6, 5]
arr1=[100, 200, 300, 400, 500]
aaa=[1, -2, 3, 4, -5, 8]
minmax(arr)
minmax(arr1)
minmax(aaa)




import re

s = '[11-09 22:55:41] [INFO ]  [  4560]'

print([float(s) if '.' in s else int(s) for s in re.findall(r'-?\d+\.?\d*', s)])