# . Write a program to input name, marks and phone number of a student and format it
# using the format function like below:
#  “The name of the student is Harry, his marks are 72 and phone number is 99999888”
"""
name = input("Enter your name:")
marks = int(input("Enter your marks:"))
Phone = int(input("Enter your phone number:"))

info = "The name of student is {} , his/her marks are {} and phone number is {}".format(name,marks,Phone)
print(info)
"""



# . A list contains the multiplication table of 7. write a program to convert it to vertical string of same numbers.

table = (str(7*i) for i in range (1,11))
vertical_table = "\n".join(table)
print(vertical_table)



# Write a program to filter a list of numbers which are divisible by 5.

mylist = [1 , 3 , 4 , 5 , 65 , 67, 195 , 255]

def divisibilitybyfive(n):
    if n%5 == 0:
        return True
    return False

five = filter(divisibilitybyfive,mylist)
print(list(five))



# Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce
g = [2 , 45 , 56 , 3 , 100]
def max(a,b):
    if(a>b):
        return a
    return b

print(reduce(max,g))




# . Explore the ‘Flask’ module and create a web server using Flask & Python.

from flask import Flask

app = Flask(__name__)

@app.route("/about")
def hello_world():
    return "<h1> Hello , My name is Gargu </h1>"

if __name__ == "__main__":
    app.run(debug=True)