print("Quick Quiz: Write a program to greet a user with “Good day” using functions.")

def greet():
    name = input("Enter your name:")
    print(f"Good day {name} .")

greet()




print("Quick Quiz: Write a program to find out average of three numbers using functions.")

def avg():
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = int(input("Enter value of c:"))

    print(a+b+c/3)

avg()





def sum(a,b,c):
    print(a+b+c)

sum()



print("Two type of Fucntions")
print("Built in function(already present in python) /n len(), print(), range()")
print("user defined function(defined by user) /n avg() , greet()")




print("Functions witn argument.")

def goodday (name):
    gr = "Hello" + name
    return gr

b = goodday(" Gargee")
print(b)




print("Default parameter value")

def default(name = " Stranger"):
    greet = ("HEllo" + name)
    return greet
b = default( )
print(b)
c = default(" GArgee")
print(c)





print("Recursion")

def factorial(n):
    
    if n==0 or n ==1 :
        return 1
    else:
        return n * factorial(n-1)
    
a =factorial(5)
print(a)