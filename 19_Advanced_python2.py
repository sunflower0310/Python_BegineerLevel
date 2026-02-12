# VENV

##  step 1 : pip install virtualenv
# step 2 : python -m venv env
#          env folder appear


# pip freeze shows all package installed in python
#  pip freeze > requirement.txt adds all this package info in requirement folder(global)
# pip install -r\requirement.txt adds in (virtual)



# LAMBDA

square = lambda a,b: a*b
print(square(2,2))

sum = lambda a,b,c:a+b+c
print(sum(1,2,3))


# JOIN
 
list = ["Banana" , "Apple" , "Grapes"]

final = " , ".join(list)
print(final)



# Index

a = "{} are female whereas {} are male but humko kya hi farak padta hai hum toh {} hai".format("Girls" , "boys" , "legends")
c = "{0} are female whereas {1} are male but humko kya hi farak padta hai hum toh {2} hai".format("Girls" , "boys" , "legends")
b = "{1} are male whereas {0} are female but humko kya hi farak padta hai hum toh {2} hai".format("Girls" , "boys" , "legends")

print(a)
print(c)
print(b)



# MAP



mylist = [1,2,3,4]

square = lambda x : x*x
sqlist = map(square , mylist)
print(list(sqlist))




# FILTER


def even(n):
    if n%2==0:
        return True
    else:
        return False
    
evenlist = filter(even,mylist)
print(list(evenlist))



# REDUCE


from functools import reduce

def sum(a,b):
    return a+b

print(reduce(sum,mylist))

def mult(a,b):
    return a*b

print(reduce(mult,mylist))

