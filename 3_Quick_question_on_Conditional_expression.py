Marks = int(input("Enter your marks :"))

if(Marks>=90 and Marks<=100):
    print("Grade A")

elif(Marks>=75 and Marks<=89):
    print("Grade B")

elif(Marks>=50 and Marks<=74):
    print("Grade C")

elif(Marks>=33 and Marks<=49):
    print("Grade D")

elif(Marks<0 or Marks>100):
    print("Invalid Marks")

else:
    print("Fail")

print("Thank you!!")
