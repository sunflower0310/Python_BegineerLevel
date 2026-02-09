# WALRUS

if(n:= len([12 , 34 ,19 , 3, 1]))>3:
    print(f"List is long({n} elements present , <= 3 expected)")




# Type Hints Beigneer Level

def sum(a:int , b:int) -> int :
    return a+b

print(sum(3,4))





# Type Hints for Large projects

from typing import List , Tuple , Dict , Union

numbers: List[int] = [1,2,3,4]

person: Tuple[str,int] = ("Alice" ,10)

scores : Dict[str,int] = {"Alice":10}

identifier : Union[int,str] = "IUY356"
identifier : 12345      
# both identifier valid   

print(person)




# Match Case

def check_status(code):
    match code:
        case 200 : 
            return "Success"
        case 301 : 
            return "Moved Permanently"
        case 404 : 
            return "Page not found"
        case 500:
            return "Server Error"
        case _:
            return "Invalid Status Code"
        
print(check_status(404))
print(check_status(333))



# Dict Merge

Student1 = {"Maths":95 , "Science" : 91}
Student2 = {"English":98 , "Science" : 89}
NewDict = Student1|Student2

print(NewDict["Science"])
print(NewDict["Maths"])




# File
"""
with (open ("file1.txt") as f1 , 
      open ("file2.txt") as f2):
"""



# Exception Handling

try:
    a = int(input("Enter value of a :"))
    b = int(input("Enter value of b :"))
    result = a/b
    print("Result:" , result)

except ZeroDivisionError  as z :
    print("You can't divide a number by zero" , z)

except ValueError as v :
    print("Please enter valid numbers" , v)

print("Program finished")





# Raising Exception 

a = int(input("Enter value of a :"))
b = int(input("Enter value of b :"))

if(b==0):
    raise ZeroDivisionError ("Can't Divide By Zero")
else:
    print(f"Result: {a/b}")





# Try el
try :
    a = int(input("Enter your number:"))

except Exception as e :
    print(e)

else:
    print("I am inside els")



# Try final
def main():
    try:
        n = int(input("Enter your name:"))
        return
    except Exception as e :
        print(e)
        return

    finally:
        print("I am inside finally")


main()




# __name__ == "__main__"
# This topic done in test.py and main.py


# Global

cake = 19
def hello():
    global cake
    print(cake)

hello()

cake = 19
def hello():
    global cake
    cake =3
    print(cake)

hello()



# Enumerate

list = [2 , 3 , 45 , 78]

# index =0
# for i in list :
#     print(f"{i} is at index {index}")
#     index += 1

# This can be done shortly

for index ,item in enumerate (list):
    print(f"{item} is at index {index}")



# List Comprehension

Mylist = [ 2 , 3 , 4 , 5]

# squared_list = []
# for item in Mylist:
#     squared_list.append(item*item)
# print(squared_list)

# This can be done shortly

squared_list = [i*i for i in Mylist]
print(squared_list)