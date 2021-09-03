"""def fun(a,b):
    return f"{(a//b)}\n{a/b}"

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(fun(a,b))


def is_leap(year):
    leap = False
    not_leap=True

    # Write your logic here
    if year%4==0:
        return leap


year = int(input())
print(is_leap(year))



"""
def dun(n):
    temp=[]
    for i in range(1,n+1):
        temp.append(str(i))
    s="".join(temp)
    return s


if __name__ == '__main__':
    n = int(input())
    print(dun(n))