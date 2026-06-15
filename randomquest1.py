# # 1. Write a program to print Twinkle twinkle little star poem in python.
# print('''Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.''')

# # # 1. Write a python program to add two numbers.
# x = 2
# y = 7
# print(x+y)

# # # 1. Write a python program to display a user entered name followed by Good
# # # Afternoon using input () function.
# name = input("Enter Your Name: ")
# print("Good Afternoon ",name)

# # # 1. Write a program to store seven fruits in a list entered by the user.
# l = []
# l1 = input("Enter The Fruit Name: ")
# l.append(l1)
# l2 = input("Enter The Fruit Name: ")
# l.append(l2)
# l3 = input("Enter The Fruit Name: ")
# l.append(l3)
# l4 = input("Enter The Fruit Name: ")
# l.append(l4)
# l5 = input("Enter The Fruit Name: ")
# l.append(l5)
# l6 = input("Enter The Fruit Name: ")
# l.append(l6)
# l7 = input("Enter The Fruit Name: ")
# l.append(l7)
# print(l)

# # # 1. Write a program to create a dictionary of Hindi words with values as their English
# # # translation. Provide user with an option to look it up!
# dic = {'Mai':'Me','Kursi':'chair','maiz':'table','kitab':'book'}
# word = input("Enter The Word: ")
# print(dic[word])

# # # 1. Write a program to find the greatest of four numbers entered by the user.
# a = int(input("Enter The Number :" ))
# b = int(input("Enter The Number :" ))
# c = int(input("Enter The Number :" ))
# d = int(input("Enter The Number :" ))
# if (a > b and  a > c and a>d):
#     print("Greatest Among The Four Is: ",a)
# elif(b > a and b > c and b > d):
#     print("Greates Among The Four Is: ",b)
# elif(c > a and c > b and c >d):
#     print("Greatest Among The Four Is: ",c)
# else:
#     print("Greatest Among The Four Is: ",d)

# # # 1. Write a program to print multiplication table of a given number using for loop.
# num = int(input("Enter The Number: "))
# for i in range(1,11):
#     print(f"{num} X {i} = {num*i}")

# # # 1. Write a program using functions to find greatest of three numbers.
# def greatest(a,b,c):
#     if (a >b and a > c):
#         print("Greatest Number = ",a)
#     elif(b > a and b > c):
#         print("Grestest Number = ",b)
#     else:
#         print("Greatest Number = ",c)
# greatest(2,5,3)

# # # 1. Write a program to read the text from a given file ‘poems.txt’ and find out
# # # whether it contains the word ‘twinkle’.
# with open("/home/arshad/Muskan/poem.txt") as f:
#     content = f.read()

# if "twinkle" in content:
#     print("Yes,Twinkle Is Present In The File")
# else:
#     print("No,Twinkle Is Not Present In The File")

# # # 1. Create a class “Programmer” for storing information of few programmers
# # # working at Microsoft.
# class Programmer:
#     def __init__(self,p_id,name,salary):
#         self.p_id = p_id
#         self.name = name
#         self.salary = salary

#     def __str__(self):
#         return(f"Programmer Id: {self.p_id},Programmer Name: {self.name},Programmer Salary: {self.salary}")

# Muskan = Programmer(1,"Muskan",35000)
# print(Muskan)

# # 1. Create a class (2-D vector) and use it to create another class representing a 3-D
# # vector
# class Vector2D:
#     def __init__(self,i,j):
#         self.i = i
#         self.j = j

# class Vector3D(Vector2D):
#     def __init__(self, i, j,k):
#         super().__init__(i, j)
#         self.k = k

#     def show(self):
#         print(f"{self.i}i + {self.j}j + {self.k}k")

# v = Vector3D(2,5,7)
# v.show()

# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not
# present, a message without exiting the program must be printed prompting the same.
# try:
#     f1 = open("/home/arshad/Muskan/1.txt")
# except FileNotFoundError:
#     print("File 1.txt Not Found")

# try:
#     f2 = open("/home/arshad/Muskan/2.txt")
# except FileNotFoundError:
#     print("File2.txt Not Found")

# try:
#     f3 = open("/home/arshad/Muskan/3.txt")
# except FileNotFoundError:
#     print("File 3.txt Not Found")

# 1. Create two virtual environments, install few packages in the first one. How do you
# create a similar environment in the second one?
# creasted sucessfully

