print("1. Create a class “Programmer” for storing information of few programmers working at Microsoft.")

class Programmer:
    company = "Microsoft"
    
    def __init__(self,name,age,language):
        self.name = name
        self.age = age
        self.language= language

Candidate1 =Programmer("Gargee" , 20 , "python")
print(Candidate1.name , Candidate1.age , Candidate1.language)

Candidate2 = Programmer("Ziyu" , 24 , "java")
print(Candidate2.name , Candidate2.age , Candidate2.language , Candidate2.company)





print("2. Write a class “Calculator” capable of finding square, cube and greet user with hello.")

class Calculator:
    
    def __init__(self,n):
        self.n = n

    @staticmethod
    def greet():
        print("HEllo")

    def square(self):
        print(f"Square of {self.n} is {self.n*self.n}")
    
    def cube(self):
        print(f"Cube of {self.n} is {self.n*self.n*self.n}")

a = Calculator(4)
a.square()

a = Calculator(5)
a.cube()




print("5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) "
"and get fare information of train running under Indian Railways.")

class Train:

    def __init__(self,start,end,noofseat,fare):
        self.start = start
        self.end = end
        self.noofseat = noofseat
        self.fare = fare

    def book_a_ticket(self):
        print(f"You booked a ticket from {self.start} to {self.end}")

    def get_status(self):
        print(f"You are on seat number {self.noofseat}")

    def get_fare(self):
        print(f"Your ticket cost {self.fare}")

    @staticmethod
    def greet():
        print("Have a nice Journey \nThanks")


passenger1 = Train("Mumbai" , "Pune" , 42 , 100)
passenger1.book_a_ticket()
passenger1.get_status()
passenger1.get_fare()
Train.greet()



    




