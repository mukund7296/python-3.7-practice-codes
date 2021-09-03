"""#Write a funtion which take one string as input to print all duplicate char in string?

l1="communication"
#dup(l1)

x={i:l1.count(i) for i in l1}
print(x)

"""

#Write a funtion which take one integer as input to print all prime number within it?

def fun(n):
    a,b=0,1
    for i in range(1,n+1):
        print(a)
        a,b=b+a,a


usr=int(input("Enter your range number"))

fun(usr)


#
