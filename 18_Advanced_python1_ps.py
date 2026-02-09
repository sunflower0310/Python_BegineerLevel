# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not 
# present, a message without exiting the program must be printed prompting the same.
try:
    with open("file.txt" , "r")as f :
        print(f.read())

except Exception as e:
    print(e)
try:
    with open("banna.txt" , "r")as f :
        print(f.read())

except Exception as e:
    print(e)    
try:
    with open("one.txt" , "r")as f :
        print(f.read()) 

except Exception as e:
    print(e) 

print("Thanks")



# 2. Write a program to print third, fifth and seventh element from a list using enumerate function.

list = ["apple" , "banana" , "mango" , "cherry" , 2 ,3 , 5 , "chickoo"]

for index, item in  enumerate (list):
    if index == 3 or index == 5 or index == 7:
        print(item)


# 3. Write a list comprehension to print a list which contains the multiplication table of a user entered number.

n = int(input("Enter number:"))

table = [n*i for i in range(1,11)]
print(table)


# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by 
# handling the ‘ZeroDivisionError’.
try:
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))

    print(a/b)

except ZeroDivisionError as v:
    print("Infinite")


# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.

n = int(input("Enter number:"))
Tablee = [n*i for i in range (1,11)]

with open("table.txt" , "a") as f:
     f.write(f" Table of {n} :{str(Tablee)}  \n")