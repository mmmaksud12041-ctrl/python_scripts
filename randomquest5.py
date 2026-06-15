# # # 5. Label the program written in problem 4 with comments.
# # # importing os module.
# import os
# # # assigning the directory path to a variable.
# dir = '/home/arshad/Muskan'
# # # printing the contents of the directory using listdir() function.
# print(os.listdir(dir))

# # # 5. Write a python program to find an average of two numbers entered by the user.
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# average = (num1/num2)/2
# print("The average of the two numbers is: ", average)

# # # Write a program to format the following letter using escape sequence
# # # characters.
# letter = "Dear Harry, \nthis python course is nice. \nThanks!"
# print(letter)

# # # Write a program to count the number of zeros in the following tuple:
# a = (7, 0, 8, 0, 0, 9)
# count = 0
# for i in a:
#     if i == 0:
#         count += 1
# print("The Number Of Zeros In The Tuple Is: ", count)

# s = {}
# # # # What is the type of 's'?
# print(type(s))

# # # 5. Write a program which finds out whether a given name is present in a list or not.
# l = ['Alice', 'Bob', 'Charlie', 'David']
# name = input("Enter The Name You Want To Search: ")
# if name in l:
#     print("The Name Is Present In The List")
# else:
#     print("The Name Is Not Present In The List")

# # # 5. Write a program to find the sum of first n natural numbers using while loop
# n = int(input("Enter The Value Of n: "))
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print("The Sum Of The First n Natural Numbers Is: ", sum)

# # # Write a python function to print first n lines of the following pattern:
# # # ***
# # # **
# # # - for n = 3
# # # *
# n = 3
# for i in range(n, 0, -1):
#     print("*" * i)

# # # 5. Repeat program 4 for a list of such words to be censored.
# l = ['Donkey','Have','Not']
# with open('/home/arshad/Muskan/word.txt') as f:
#     data = f.read()
#     with open('/home/arshad/Muskan/word.txt', 'w') as f:
#         for word in l:
#             data = data.replace(word, '#####')
#         f.write(data)

# # # 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# # # and get fare information of train running under Indian Railways.
# from random import randint

# class Train:
#     def __init__(self,Trainno):
#         self.trainno = Trainno

#     def bookticket(self,fro,to):
#         self.fro = fro
#         self.to = to        
#         print(f"Your ticket from {self.fro} to {self.to} has been booked")

#     def getstatus(self):
#         print("No Of Seats Available are ",randint(1,100))
        
#     def getfare(self,fro,to):
#         print(f"The Ticket Fare For train {self.trainno} from {self.fro} to {self.to} is {randint(1,1000)}")

# a = Train(1245)
# a.bookticket("Pune","Solapur")
# a.getstatus()
# a.getfare("Pune","Solapur")

# # 5. Write a class vector representing a vector of n dimensions. Overload the + and *
# # operator which calculates the sum and the dot(.) product of them.

# class Vector:
#     def __init__(self,x,y,z):
#         self.x = x
#         self.y = y
#         self.z = z

#     def __add__(self,other):
#         return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
#     def __mul__(self,other):
#         return self.x * other.x + self.y * other.y + self.z * other.z
    
#     def __str__(self):
#         return f"({self.x}, {self.y}, {self.z})"
    
# v = Vector(1,2,3)
# v2 = Vector(4,5,6)
# print("The Sum Of The Two Vectors Is: ",v+v2)
# print("The Dot Product Of The Two Vectors Is: ",v*v2)

# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.
# n = int(input("Enter The Number: "))
# l = [n*i for i in range(1,11)]
# print(l)
# with open("/home/arshad/Muskan/Tables.txt","w") as f:
#     f.write(str(l))

# 5. Write a program to find the maximum of the numbers in a list using the reduce
# function.
# from functools import reduce
# l = [3,5,7,2,8,1]
# def max_num(a,b):
#     if a > b:
#         return a
#     return b
# max = reduce(max_num,l)
# print("The Maximum Number In The List Is: ",max)