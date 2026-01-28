
print("1. Write a program to read the text from a given file 'poems.txt' and find out "
"whether it contains the word 'twinkle'")


with open("poem.txt" , "r") as f:
    content =f.read()
    if("Twinkle" in content):
        print("YES! The word 'Twinkle' is present in poem.txt")
    else:
        print("NO! The word 'Twinkle' not present in poem.txt")




print("2. The game() function in a program lets a user play a game and returns the score" 
"as an integer. You need to read a file 'Hi-score.txt' which is either blank or" 
"contains the previous Hi-score. You need to write a program to update the"
 "Hiscore whenever the game() function breaks the Hi-score.")


def game():
    score = (input("Enter your score:"))

    with open ("Hi-score.txt" , "r") as f:
        highscore = f.read()
        if highscore == "":
            highscore = 0
        else:
            highscore = int(highscore)

    if score > highscore :
        with open("Hi-score.txt" , "w") as f:
            f.write(str(score))
    
    return score

game()





print("3. Write a program to generate multiplication tables from 2 to 20 and write it to the" 
"different files. Place these files in a folder for a 13  year old.")


def generatetables(n):
    table = "" 
    for i in range (1,11):
        table += f"{n} X {i} = {n*i} \n"

    with open(f"table/table_{n}.txt" , "w") as f:
        f.write(table)


for i in range(2,21):
    generatetables(i)





print("4. A file contains a word “Donkey” multiple times. You need to write a program "
"which replace this word with ##### by updating the same file.")


word = "Donkey"
with open("one.txt" , "r") as f:
    content = f.read()

contentnew = content.replace(word , "####")

with open("one.txt" , "w") as f:
    f.write(contentnew)





print("5. Repeat program 4 for a list of such words to be censored.")


List = ["Tianxuning" , "update" , "smile" , "cute"]

with open("file.txt" , "r") as f:
        content = f.read()
for i in List:
    content = content.replace(i,"#"*len(i))

with open("file.txt" , "w") as f:
    f.write(content)




print("6. Write a program to mine a log file and find out whether it contains 'python'.")


word = "Python"
with open("log.txt" , "r") as f:
    content = f.read()
if(word in content):
    print("Yes! The word python is there  in log.txt")
else:
    print("NO! The word python is not there  in log.txt")





print("7. Write a program to find out the line number where python is present from ques 6.")


with open("log.txt") as f:
    lines = f.readlines()
    
lineno = 1
for line in lines:
    if("Python" in line):
        print(f"python in {lineno}")
        break
    lineno+=1
else:
    print("python absent")

    


print("8. Write a program to make a copy of a text file “this. txt”")


with open("this.txt" , "r") as f:
    content = f.read()

with open("hello.txt" , "w") as f:
    f.write(content)





print("9. Write a program to find out whether a file is identical & matches the content of another file.")


with open("hello.txt" , "r") as f:
    hello = f.read()

with open("this.txt" , "r") as f:
    this = f.read()

if hello == this :
    print("Yupp , content matched")
else:
    print("Oops , content didn't matched")




print("10. Write a program to wipe out the content of a file using python.")


with open("wipe.txt" , "w") as f:
    f.write(" ")
    



