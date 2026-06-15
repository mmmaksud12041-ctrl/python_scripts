# # # 1. Write a program to print Twinkle twinkle little star poem in python.
# # # Done

# # # 2. Write a python program to find remainder when a number is divided by z.
# x = int(input("Enter The Number To Be Divided: "))
# z = int(input("Enter The Divisor: "))
# r = (x%z)
# print(f"When {x} Is Divided By {z} Then Remainder = {r}")

# # # Write a program to fill in a letter template given below with name and date.
# letter = '''
#     Dear <|Name|>,
#     You are selected!
# <|Date|>
# '''
# newletter = letter.replace("<|Name|>","Muskan").replace("<|Date|>","Feb 09 2026")
# print(newletter)

# # # 2. Write a program to accept marks of 6 students and display them in a sorted
# # # manner.
# marks = []
# m1 = int(input("Enter The Marks: "))
# marks.append(m1)
# m2 = int(input("Enter The Marks: "))
# marks.append(m2)
# m3 = int(input("Enter The Marks: "))
# marks.append(m3)
# m4 = int(input("Enter The Marks: "))
# marks.append(m4)
# m5 = int(input("Enter The Marks: "))
# marks.append(m5)
# m6 = int(input("Enter The Marks: "))
# marks.append(m6)
# marks.sort()
# print(marks)

# # # 2. Write a program to input eight numbers from the user and display all the unique
# # # numbers (once).
# s = set()
# n1= int(input("Enter The Number: "))
# s.add(n1)
# n2= int(input("Enter The Number: "))
# s.add(n2)
# n3= int(input("Enter The Number: "))
# s.add(n3)
# n4= int(input("Enter The Number: "))
# s.add(n4)
# n5= int(input("Enter The Number: "))
# s.add(n5)
# n6= int(input("Enter The Number: "))
# s.add(n6)
# n7= int(input("Enter The Number: "))
# s.add(n7)
# n8= int(input("Enter The Number: "))
# s.add(n8)
# print(s)

# # # 2. Write a program to find out whether a student has passed or failed if it requires a
# # # total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# # # take marks as an input from the user.

# s1 = int(input("Enter The Marks For Subject 1: "))
# s2 = int(input("Enter The Marks For Subject 2: "))
# s3 = int(input("Enter The Marks For Subject 3: "))

# p = ((s1+s2+s3)/300)*100
# print("Your Percentage Is: ",p)
# if (s1>=33 and s2>=33 and s3>=33 and p>=40):
#     print("Pass")
# else:
#     print("Fail")

# # # 2. Write a program to greet all the person names stored in a list ‘l’ and which starts
# # # with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]
# for i in l:
#     if i.startswith("S") == True:
#         print("Hello ,",i)

# # # 2. Write a python program using function to convert Celsius to Fahrenheit.
# c= int(input("Enter The Temperature In Celsius: "))
# f =  (c * (9/5)) + 32
# print(f"{c} degree is {f} Fahrenheit")

# # # 2. The game() function in a program lets a user play a game and returns the score
# # # as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# # # contains the previous Hi-score. You need to write a program to update the Hi-
# # # score whenever the game() function breaks the Hi-score.

# import random
# def game():
#     print("You Are Now Playing The Game")
#     score = random.randint(1,51)
    
#     with open("/home/arshad/Muskan/Hiscore.txt") as f:
#         Hiscore = f.read()
#         if Hiscore != "":
#             Hiscore = (int(Hiscore))
#         else:    
#             Hiscore = 0
            

#     print("Your Score Is:",score)
#     if (score > Hiscore):
#          with open("/home/arshad/Muskan/Hiscore.txt","w") as f:
#             f.write(str(score))
#     return score
# game()        

# # # 2. Write a class “Calculator” capable of finding square, cube and square root of a
# # # number.

# class Calculator:
#     def __init__(self,n):
#         self.n = n
#     def square(self):
#         return(self.n*self.n)

#     def cube(self):
#         return(self.n*self.n*self.n)
    
#     def squarert(self):
#         return (self.n**0.5)
# num = Calculator(4)
# print("Square: ",num.square())
# print("Cube: ",num.cube())
# print("Square Root: ",num.squarert())

# # 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from
# # ‘Pets’. Add a method ‘bark’ to class ‘Dog’.
# class Animals:
#     pass
# class Pets(Animals):
#     pass
# class Dog(Pets):
#     @staticmethod
#     def bark():
#         print("Bhoww Bhoww!!")

# d = Dog()
# d.bark()

# 2. Write a program to print third, fifth and seventh element from a list using enumerate
# function.
# l = [1,3,5,7,8,7,9]
# for i in enumerate(l):
#     if i[0] == 2 or i[0] == 4 or i[0] == 6:
#         print(i[1])

# 2. Write a program to input name, marks and phone number of a student and format it
# using the format function like below:
# “The name of the student is Harry, his marks are 72 and phone number is 99999888”
# name = input("Enter The Name Of The Student: ")
# marks = int(input("Enter The Marks Of The Student: "))
# phone = int(input("Enter The Phone No. Of The Student: "))
# f_string = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone)
# print(f_string)