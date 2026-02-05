# 1. Create a class (2-D vector) and use it to create another class representing a 3-Dvector.

class twoDvector:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def showtwoDvector(self):
        print(f"{self.i}i + {self.j}j")

class threeDvector(twoDvector):
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    
    def showthreeDvector(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")

a = twoDvector(2,3)
a.showtwoDvector()

b = threeDvector(3,4,5)
b.showthreeDvector()
b.showtwoDvector()




# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animals:
    def showanimal(self):
        print(f"{self.name} is a animal.")

class Pets(Animals):
    def showpets(self):
        print(f"{self.name} is a pet animal")
name = Pets()

class Dog(Pets):
    sound = "Bark"
    def showdog(self):
        print(f"Dog makes sound {self.sound}")

a = Animals()
a.name = "Cat"
a.showanimal()

p = Pets()
p.name = "Cow"
p.showpets()
p.showanimal()

d = Dog()
d.name = "Dog"
d.showdog()
d.showanimal()
d.showpets()




# 3. Create a class ‘Employee’ and add salary and increment properties to it.

class Employee:
    salary = 250
    increment = 20

    @property
    def salaryafterincrement(self):
        return (self.salary*(1+self.increment/100))
    
    @salaryafterincrement.setter
    def salaryafterincrement(self,finalsalary):
        self.increment = ((finalsalary/self.salary)-1)*100
    
e = Employee()
e.increment = 30
print(e.salaryafterincrement)

e.salary = 10000
e.increment = 100
print(e.salaryafterincrement)

f = Employee()
e.salary = 500
e.salaryafterincrement = 10000
print(e.increment)



# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded 
# operators ‘+’ and ‘*’ which adds and multiplies them.

class complex:
     
    def __init__(self, real , imag):
        self.real = real
        self.imag = imag

    def __add__(self,other):
        real_part = self.real + other.real
        imag_part = self.imag + other.imag
        return complex (real_part , imag_part)
    
    def __mul__(self,other):
        real_part = self.real*other.real - self.imag*other.imag
        imag_part = self.real*other.imag + self.imag*other.real
        return complex (real_part , imag_part)
    
    def __str__(self):
        return f"{self.real} + {self.imag}i"
    

c1 = complex(2,3)
c2 = complex(4,5)

sum_result =c1+c2
mul_result = c1*c2

print("Addition: " , sum_result)
print("Multiplication: " , mul_result)