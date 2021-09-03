#Q1: Find the loop elemnets
def funn(x):
    a,b,c=x[0],x[1],x
    for i in range(len(a)):
        if a[i] in a and a[i] in b:
            print(a[i],a,b)
        elif a[i] in a:
            print(a[i],a)
        else:
            print(a[i],b)
       # print(x[0][i],": [",x[1],",",x[0],"]")

v=["rahul","suhash"]
funn(v)

print("*"*30)
#Q2 Q2  create a list and append data into that list and print list element s:

class Vehicle:
    def __init__(self,a,b):
        self.a=a
        self.b=b



list1=[]

list1.append(Vehicle("MH11",40435454))
list1.append(Vehicle("MH12",10435454))
list1.append(Vehicle("MH13",50435454))
list1.append(Vehicle("MH14",33335454))

for i in list1:
    print(i.a,"-",i.b)
print("*"*30)

#Q3 Find the minimum and maximum sum of N-1 elements of the array

#Examples: Input: a[] = {13, 5, 11, 9, 7}
#Output: 32 40

def minmax(n):
    a=sorted(n)
    mini=0
    max=0
    ll=len(n)
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
print("*"*30)
#4
x=sorted(aaa)
print(x)

#4 program to Remove leading zeros from an IP

import re

rem='\.[0]*'

def remo(x):
    modi=re.sub(rem,'.',x)
    return modi
c="216.08.094.196"

print(remo(c))

