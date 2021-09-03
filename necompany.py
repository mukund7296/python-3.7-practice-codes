
a = [[]]*5
print(a)

a = [()]*5
print(a)

a = [{}]*5
print(a)

l1=[1,2,3]
l2=[1,2,3]
l3=l2
print(id(l1),id(l2),id(l3))

from collections import Counter
MyList = ["a", "b", "a", "c", "c", "a", "c"]

x=Counter(MyList)
print(x)
data={i:MyList.count(i) for i in MyList}
print(data)


weekdays = ['sun','mon','tue','wed','thu','fri','sun','mon','mon']
print([[x,weekdays.count(x)] for x in set(weekdays)])

names = ['Chris', 'Jack', 'John', 'Daman']
print(names[-1][-1])

subjects = ('Python', 'Interview', 'Questions')
for i,subjects in enumerate(subjects):
    print(i,subjects)

items = set()

# Add three strings.
items.add("Python")
items.add("coding")
items.add("tips")

print(items)

print (sum(range(1,101)))

import wordninja

x="chinaindiausa"
print(wordninja.split(x))