def pyfun(r):
    for a in range(r):

        print(' '*(r-a-1)+'*'*(2*a+1))

pyfun(9)
list = [ "13", "16", "1", "5" , "8"]
list=[int(i) for i in list]
list.sort()
print(list)