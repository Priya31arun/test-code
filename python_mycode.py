import math
import string

#**** Variable and data storin***

# Name = "Krish"
# Age = "8"
# He_is_student = "yes"
# print("Name =",Name)
# print("Age =",Age)
# print("He_is_student =",He_is_student)

# #*** User Input***

# userinput = input ("Enter your name =")
# print("Hello Mr",userinput)

# #*** if else (condition)***
# age =int(input("Enter your age:"))
# if age >= 18:
#     print("you are an adult")
# else :     
#     print("you are an minor")

# #*** List and Loops***

# vegetables = ["tomatto","pottato","beans"]
# # print(vegetables[0]+"\n"+vegetables[1]+"\n"+vegetables[2])
# for vegetable in vegetables:
#     print(vegetable)
# vegetables.append("carrot")
# vegetables.append("onion")
# print("Updated vegetables list:")
# for vegetable in vegetables:
#     print(vegetable)
# vegetables.remove("pottato")
# print("after removing pottao final vegetables list:")
# print(*vegetables, sep="\n")

#Functions#

def say(person):
    return f"Hello, {person}!"

print(say("Arun"))

def square(number):
    return number ** 2

print("Square of 5:", square(5))
   