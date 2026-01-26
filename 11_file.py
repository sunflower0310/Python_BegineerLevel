print("Reading a file")
f = open("one.txt" , "r")
text = f.read()
print(text)




print("Writing a file")
f = open("one.txt" , "w")
text = f.write("Be nonchalant")




print("Using readline")


f = open("one.txt", "r")
txt = f.readline()
while txt!="":
    print(txt)
    txt=f.readline()




print("Using append")


txt = " Although right now my life is fucked up but one day this darkness will end "
f = open("one.txt" , "a")
A= f.write(txt)
print(A)




print("using with")


with open("one.txt" , "r") as f:
    print(f.read())

