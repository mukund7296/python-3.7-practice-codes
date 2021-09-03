from collections import Counter
MyList = ["a", "b", "a", "c", "c", "a", "c"]

x=Counter(MyList)
print(x)
#----------------------------------------------
b={i:MyList.count(i) for i in MyList}

print(b)

sampleList = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", sampleList)

countDict = dict()
for item in sampleList:
    if(item in countDict):
        countDict[item] += 1
    else:
        countDict[item] = 1

print("Printing count of each item  ",countDict)


MyList = ["a", "b", "a", "c", "c", "a", "c","a", "b", "a", "c", "c", "a", "c"]

v={i:MyList.count(i) for i in MyList}
print(v)

def pyfunc(r):
    for x in range(r):
        print(' '*(r-x-1)+'*'*(2*x+1))
pyfunc(9)


d = {'abc': 'xyz', (1,2,3) : 'pqr'}
print(d)


"""
days = {'Mon', 'Tue'}
days.add([1,2,3])
print(days)"""


