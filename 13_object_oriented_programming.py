
class Students:
    School = "Public School"
    Division = "10th"
    Age = "15"

Rollno1 = Students()
Rollno1.name = "Gargee"
Rollno1.hobby = "Drawing"
print(Rollno1.name , Rollno1.Division , Rollno1.hobby)

Rollno2 = Students()
Rollno2.name = "Ziyu"
Rollno2.hobby = "Singing"
Rollno2.Age = "19"
print(Rollno2.name , Rollno2.Age , Rollno2.Division)
# instance attribute take over class attribute

# self parameter


class Employee:
    Company = "Microsoft"
    Age = 23
    City = "Pune"
    Working_hour = "9_to_5"

    def getinfo(self):
        print(f"Name of Employee is {self.name} \n Age is {self.Age} \n Company he works in {self.Company}")

    def greet(self):
        print(f"Good morning ")

    @staticmethod
    def end():
        print(f"Good day")
# when we need a function that does not use self parameter we use static method

Ziyu = Employee()
Ziyu.name = "Fish"
Ziyu.greet()
Ziyu.getinfo()

Gargee = Employee()
Gargee.greet()
Gargee.end()


class people:
    planet = "Earth"

    def __init__(self , name , city , age ,):
        self.name = name 
        self.city=city
        self.age = age

Tianxuning = people("Tianlie" , "Beijing" , 27)
print(Tianxuning.name , Tianxuning.city , Tianxuning.age )