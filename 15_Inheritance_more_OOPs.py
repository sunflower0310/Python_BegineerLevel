# Inheritance
class Animal:
    category = "Living Being"
    
    def show_name(self):
        print(f"{self.name} is a {self.category} animal.")

name = Animal()

class Dog(Animal):
    sound = "Bark"

    def show_sound(self):
        print(f" {self.name} is a {self.category} and makes sound as {self.sound}.")

name = Dog()

a = Animal()
d = Dog()

a.name = "Cat"
a.show_name()

d.name = "Dog"
d.show_name()
d.show_sound()
# a.show_sound() this will show error

# Multiple Inheritance

class College:
    college_name = "MIT WPU"

    def show_college(self):
        {f" {self.college_name} college."}

class Course:
    course_name = "BCA"

    def show_course(self):
        {f"Course is {self.course_name}"}

class Student(College,Course):

    def show_details(self):
        print(f"{self.name} chose {self.course_name} in {self.college_name}")

name = Student()


a = College()
b = Course()
c= Student()

c.name = "Gargee"
c.show_details()

# Multilevel Inheritance

class Vehicle:
    type = "transport"

    def show_type(self):
        print(f"{self.type}")

class Car(Vehicle):
    wheels = 4

    def show_wheels(self):
        print(f"{self.wheels}")

class ElectricCar(Car):

    def show_brand(self):
        print(f"{self.brand}")
brand = ElectricCar()

v = Vehicle()
c = Car()
e = ElectricCar()

v.show_type()
c.show_type()
e.show_type()
e.show_wheels()

# Super

class Company:

    def __init__(self):
        print("Company Constructor")
    a = 1

class Employee(Company):

    def __init__(self):
        super().__init__()
        print("Employee Constructor")
    b = 2

c = Company()
e = Employee()




# Class Method


class Employee:
    a = 1

    @classmethod
    def show(self):
        print(f"hello {self.a}")

    def showobject(self):
        print(f"Goodbye {self.a}")


e = Employee()

e.a = 3
e.show()

e.showobject()


# Property Decorator


class student:
    a = 1

    @property
    def fullname(self):
        return (f"Student Name: {self.first} {self.middle} {self.last}.")

    @fullname.setter
    def fullname(self,value):
        self.first = value.split(" ")[0]
        self.middle = value.split(" ")[1]
        self.last = value.split(" ")[2]


s = student()
s.fullname = "Ziyu Tian Xuning"
print(s.fullname)

h = student()
h.fullname = "Rahul Kumar Sharma"
print(h.fullname)
        


# Operator Overloading

class Money:

    def __init__(self,amount):
        self.amount = amount

    def __add__(self,other):
        return self.amount + other.amount 
    

m1 = Money(100)
m2 = Money(200)
print(m1 + m2 )



class length:
    def __init__(self,n):
        self.n = n

    def __len__(self):
        return (len(self.n))
    
l = length("Gargee")
print(len(l))


class string:

    def __init__(self,word):
        self.word = word

    def __str__(self):
        return (str(self.word))
    
s = string("Gargee")
print(str(s))


class Book:

    def __init__(self,word):
        self.word = word

    def __len__(self):
        return (len(self.word))
    
    def __str__(self):
        return str(self.word)
    

b = Book("Harry Potter")
print(len(b))
print(b)

