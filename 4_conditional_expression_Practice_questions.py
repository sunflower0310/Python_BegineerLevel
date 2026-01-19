print("1. Write a program to find the greatest of four numbers entered by the user.")


a =int(input("Enter the value of a:"))
b =int(input("Enter the value of b:"))
c =int(input("Enter the value of c:"))
d =int(input("Enter the value of d:"))

if(a>b and a>c and a>d):
    print("The greatest number is" , a)

elif(b>a and b>c and b>d):
    print("The greatest number is" , b)

elif(c>a and b<c and c>d):
    print("The greatest number is" , c)

elif(d>a and d>c and b<d):
    print("The greatest number is" , d)


    


print("2. Write a program to find out whether a student has passed or failed if it requires a"
 "total of 40% and at least 33% in each subject to pass. Assume 3 subjects and" 
 "take marks as an input from the user.")


E = int(input("Enter marks of English :"))
M = int(input("Enter marks of Maths :"))
S = int(input("Enter marks of Science :"))

P = (100*(E + M + S))/300

if ( P>= 40 and E >=33 and M>=33 and S>=33):
    print(f"You passed exam with  {P} % .  ")

else :
    (f"You are fail with {P} %")



    

print("3. A spam comment is defined as a text containing following keywords“Make a lot of money”," 
"“buy now”, “subscribe this”, “click this”. Write a program "
"to detect these spams") 


S1 = "Make a lot of money"
S2 = "buy now"
S3 = "subscribe this"
S4 = "click this"

C = input("Enter Comment :")

if(S1 in C or S2 in C or S3 in C or S4 in C):
    print("This is a spam comment.")

else:
    print("This is not a spam comment.")





print("4. Write a program to find whether a given username contains less than 10 characters or not.")


User_name = input("Enter User name:")

if(len(User_name) == 10 ):
    print(f"Your username {User_name} contains 10 character")

else:
    print(f"Your username {User_name} doesn't contains 10 character")





print("5) Write a program which finds out whether a given name is present in a list or not")


l =["Gargee" , "Tianxuning" , "Ziyu" ]

N = input("Enter name:")

if(N in l):
    print("Your name is present in List")

else:
    print("Your name is not present in List")





print( "6) Write a program to find out whether a given post is talking about “Tianxuning” or not.")


P = input("Enter post :")

if("Tianxuning" in P):
    print("Yes ")

else:
    print("NO")