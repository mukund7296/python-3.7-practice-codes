
i=0
while i<10:
    i+=1
    print(i,end=",")
print()
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

user=int(input("Enter your number for factorial :"))
print(user,": Factorial is ",fact(user))

# Program to double each item in a list using map()

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2 , my_list))

print(new_list)