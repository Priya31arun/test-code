import math
import string

# #**** Variable and data storing***

# # Name = "Krish"
# # Age = "8"
# # He_is_student = "yes"
# # print("Name =",Name)
# # print("Age =",Age)
# # print("He_is_student =",He_is_student)

# # #*** User Input***

# # userinput = input ("Enter your name =")
# # print("Hello Mr",userinput)

# # #*** if else (condition)***
# # age =int(input("Enter your age:"))
# # if age >= 18:
# #     print("you are an adult")
# # else :     
# #     print("you are an minor")

# # #*** List and Loops***

# # vegetables = ["tomato","potato","beans"]
# # # print(vegetables[0]+"\n"+vegetables[1]+"\n"+vegetables[2])
# # for vegetable in vegetables:
# #     print(vegetable)

# # vegetables.append("carrot")
# # vegetables.append("onion")
# # print("Updated vegetables list:")
# # for vegetable in vegetables:
# #     print(vegetable)

# # vegetables.remove("potato")
# # print("after removing potato final vegetables list:")
# # print(*vegetables, sep="\n")

# #Functions#

# def say(person):
#     return f"Hello, {person}!"

# print(say("Arun"))

# def square(number):
#     return number ** 2 
# print("enter the number:")
# number = int (input())
# result = square(number)
# print(f"The square of {number} is {result}")

# def cube(number):
#     return number ** 3
# print("enter the number which you wants to cube:")
# number = int(input())
# result = cube(number)
# print(f"the cube of the {number} is {result}")

# def square(floatnumber):
# #  return floatnumber ** 2 
# # print ("enter the number you wants to make floating number with sqaure:")
# # num_str = input()
# # fnumber = float(num_str)
# # result = square(fnumber)
# # print(f"The float of your input is {fnumber}")
# # print(f"The square of {fnumber} is {result}")

# secret_number=6
# attempts=0 #(before i mentoned 1)
# while True:
#     guess = int (input("Guess a number between 1 and 10:"))
#     attempts +=1
#     if guess>secret_number:
#         print("Too high")
#     elif guess<secret_number:
#         print("Too low")
#     else:
#         print("Congrats your gussed number is correct!")

#         break
#     print(f"you took {attempts}attempt(s).")



# 1. Arithmetic Operators

a = 10
b = 3

print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus (Remainder):", a % b)
print("Exponentiation:", a ** b)
print()

# # 2. Comparison Operators

print("Comparison Operators:")
print("Equal to:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater or Equal:", a >= b)
print("Less or Equal:", a <= b)
print()

# # 3. Assignment Operators

x = 5
print("Assignment Operators:")
print("Initial x:", x)
x += 2
print("x after x += 2:", x)
x -= 1
print("x after x -= 1:", x)
x *= 3
print("x after x *= 3:", x)
x /= 2
print("x after x /= 2:", x)
x **= 2
print("x after x **= 2:", x)
print()

# # 4. Logical Operators
p = True
q = False
print("Logical Operators:")
print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)
print()

# # 5. Membership Operators
my_list = [1, 2, 3, 4, 5]
print("Membership Operators:")
print("Is 3 in the list?", 3 in my_list)
print("Is 10 not in the list?", 10 not in my_list)
print("Is 'string' in my_list?", 'string' in my_list)
print()

# # 6. Identity Operators
x = [1, 2]
y = [1, 2]
z = x  # z points to the same object as x

print("Identity Operators:")
print("x is y:", x is y)           # False (different objects with same values)
print("x is z:", x is z)           # True (same object)
print("x is not y:", x is not y)   # True

