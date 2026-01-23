print("1. Write a program using functions to find greatest of three numbers")

def greatest(a,b,c):
    if(a>b and a>c):
        return(f"{a} is greatest of all three")
    elif(b>a and b>c):
        return(f"{b} is greatest of all three")
    elif(c>b and c>a):
        return(f"{c} is greatest of all three")
        
print(greatest(2,3,4))




print("2. Write a python program using function to convert Celsius to Fahrenheit.")

def C_to_F(c):
    formula =  (c*9/5 )+32
    return(f"{c} in Fahrenheit is {formula}.")

print(C_to_F(12))





print("3. How do you prevent a python print() function to print a new line at the end.")

print("a" , end ="")
print(" b" , end ="")
print(" c" , end ="")






print("4. Write a recursive function to calculate the sum of first n natural numbers")

def natural_numbers(n):
    if (n==0 or n==1):
        return 1
    else:
        return natural_numbers(n-1)+n
    
print(natural_numbers(4))




print("5. Write a python function to print first n lines of the following pattern"
"***"
"**   for n = 3"
"*")

def stars(n):
    if (n==0):
        return
    else:
        print("*"*n)
        stars(n-1)

print(stars(4))



print("6. Write a python function which converts inches to cms.")
def inch_cm(n):
    return (f"Value of {n} inch in cm is {n*2.54}.")

print(inch_cm(4))




print("7. Write a python function to remove a given word from a list ad strip it at the same time.")

def remove(l,word):
    n =[]
    for i in l:
        if not i==word:
            n.append(i.strip(word))
    return n

l = ["Hello" , "Welcome" , "Bye" , "nihao"]
print(remove(l,"Hello"))






print("8. Write a python function to print multiplication table of a given number.")

def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
        
table(5)
    
