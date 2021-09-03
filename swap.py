
def clean_text(s: str) -> str:
    '''replace a, b, c characters with asterisk - *'''
    temp=[]
    for i in s:

        if i=="a" or i=="b" or i=="c":
            temp.append("*")
        else:
            temp.append(i)
    print("".join(temp))


s = 'string sample'
#   clean_text(s) == 'string s*mple'
print(clean_text(s))


"""


Codeshare logo
ShareSign UpLog In
1
​
2
def mydecorator():
    3
def wrapper():
4
print("Welcome to our website")
5

6
return add()
7
print("thanks ")
8
​
9
​
10
@mydecorator                      # property decorator
11
def add(self.a,b):
12
return a+b
13
​
14
@classmehtod                     #
15
def funnn(cls)
    16
​
17
@static method
18
def fun():
    19

20
​
21

22
def clean_text(s: str) -> str:
    23
'''replace a, b, c characters with asterisk - *'''
24
temp=[]
25
for i in s:
26

27
if i=="a" or i=="b" or i=="c":
28
temp.append("*)
29
else:
30
temp.append(i)
31
print(temp)
32

33
​
34
s = 'string sample'
35
clean_text(s) == 'string s*mple'
36
​

"""


