#1 question :
string = 'abc'
#string[2] = 'z'
print(string)

# we cant add between string like this
# TypeError: 'str' object does not support item assignment
#2 nd question
string = 'abc'
print(id(string))
string = string + 'xyz'
print(string)
print(id(string))

"""
Out put 
abc
30734520 #immutable its change the memory address
abcxyz
36111392 #immutable
"""
#3 rd question is it shows same memory location.
s = 'abc'
s1 = 'abc'
print(s,s1)
print(id(s),id(s1))
"""
output 3:
abc abc
34076856 34076856

"""
#4 question

l = ['abc', 'xyz']
l1=['abc', 'xyz']
"""
it will Not show same address 
"""
print(id(l),id(l1))

l = ['abc', 'xyz']
l1 = l
print(id(l),id(l1))
# this time it will show same memory address
"""
#question 6  cant possible with list
d = {'abc': 'xyz', [1,2,3] : 'pqr'}
print(d)
#answer TypeError: unhashable type: 'list'
"""
#with tuple this is possible
d = {'abc': 'xyz', (1,2,3) : 'pqr'}
print(d)
#{'abc': 'xyz', (1, 2, 3): 'pqr'}

days = {'Mon', 'Tue'}
days.add([1,2,3])

print(days)
# cant possible TypeError: unhashable type: 'list'
days = {'Mon', 'Tue'}
days.add((1,2,3))
print(days)
# output {'Mon', 'Tue', (1, 2, 3)}
try:
    a = 1/0
except:
    print('A')
else:
    print('B')
finally:
    print('C')
#TypeError: unhashable type: 'list'
"""

From Sayali to Everyone:  04:06 PM
a = [[]]*5
#output [],[],[],[],[]

From Me to Everyone:  04:07 PM
[]
From Sayali to Everyone:  04:11 PM
try:
    a = 1/0
except:
    print('A')
else:
    print('B')
finally:
    print('C')
class A:
    pass

class B(A):
    pass

class C:
    pass

class D(B,C):
    pass
D.__mro__
__init__ and __new__ and __call__
"""

__init__ and __new__ and __call__