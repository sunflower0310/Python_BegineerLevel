print("1. Write a program to print multiplication table of a given number using for loop.")

num = int(input("Enter number:"))

for i in range(1,11):
    print(f"{num} X {i} = {num*i}")




print("2. Write a program to greet all the person names stored in a list ‘l’ and which starts with s.")

l = ["Harry", "Soham", "Sachin", "Rahul"]

for i in l :
    if (i.startswith("S")):
        print(f"Hello {i}")




print("3. Attempt problem 1 using while loop")

num = int(input("Enter number:"))
i =1
while(i<11):
    print(f"{num} X {i} = {num*i}")
    i+=1





print("4. Write a program to find whether a given number is prime or not.")

n = int(input("Enter number:"))

for i in range(2,n):
    if(n%i == 0):
        print(f"{n} is not prime.")
        break

    else:
        print(f"{n} is prime")
        break




print("5. Write a program to find the sum of first n natural numbers using while loop.")

n = int(input("Enter number:"))

i = 1
sum = 0

while i<=n :
    sum = sum + i
    i += 1
print(sum)





print("6. Write a program to calculate the factorial of a given number using for loop")

n = int(input("Enter number:"))
for i in range(1,n):
    if(n%i == 0):
        print(i)




print("7. Write a program to print the following star pattern.")
#   *
#  ***
# ***** for n = 3

n = int(input("Enter n:"))
for i in range(1,n+1):
    print(" " * (n-i) , end=" ")
    print("*" * (2*i-1) , end=" ")
    print(" ")






print("8. Write a program to print the following star pattern")
# *
# **
# *** for n = 3

n = int(input("Enter n :"))
for i in range(1,n+1):
    print("*" * i , end=" ")
    print(" ")





print("9. Write a program to print the following star pattern")
# * * *
# *   *    for n = 3
# * * *

n = int(input("Enter n :"))

for i in range(1 , n+1):
    if(i==1 or i==n):
        print("*" * n)
    else:
        print("*" , end="")
        print(" " * (n-2) , end="")
        print("*" , end="")
        print(" ")





print("10. Write a program to print multiplication table of n using for loops in reversed order.")

n = int(input("Enter number:"))
for i in range(1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")

