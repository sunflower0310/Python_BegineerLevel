import random 

c = random.choice([-1,0,1])
compdict = {-1: "Snake" , 0: "Water" , 1: "Gun"}
youdict = {"Snake": -1 , "Water": 0 , "Gun": 1}

user = input("Enter Your choice:").capitalize()
u = youdict[user]


print(f"You choosed {compdict[u]} and Computer choosed {compdict[c]}.")

if (u==c ):
    print("DRAW!")
elif(u== -1 and c==0):
    print("You won!")
elif(u== 0 and c==-1):
    print("You lose!")
elif(u== 0 and c==1):
    print("You won!")
elif(u== 1 and c==0):
    print("You loose!")
elif(u== -1 and c==-1):
    print("You won!")
elif(u== -1 and c==1):
    print("You lose!")

else:
    print("Something whent wrong.")