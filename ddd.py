
def mydec(func):
    gitt=func("Hello everyone ")
    return gitt

def title(txt):
    return txt.upper()

def name(txt):
    return txt.lower()

print(mydec(title))
print(mydec(name))


def bubbleSort(n):
    x=len(n)
    for i in range (x):
        for j in range(i + 1, x):
            if(n[i] > n[j]):
                temp = n[i]
                n[i] = n[j]
                n[j] = temp
    print(n)

B=[64, 34, 25, 12, 22, 11, 90]
bubbleSort(B)