list1=[1,2,3,4,5,6,7,8,9]

def rev(n):
    expected=[]
    for i in list1[::-1]:
        if i%2==1:
            expected.append(i)
    for i in list1:
        if i%2==0:
            expected.append(i[::2])
    print(expected)

rev(list1)

list2=[9,2,7,4,5,6,3,8,1]



for i in range( len(list1) - 1, -1, -1) :
    print(list1[i])

#select top1 salary from (select top 2 salary from emp order by salary desc) as emp order by salary asc:

