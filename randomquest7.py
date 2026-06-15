# 7.
# 7.
# 7.
# 7.
# 7. If the names of 2 friends are same; what will happen to the program in problem
# 6?
# d = {}
# for i in range(1,5):
#     key = input("Enter Your Name: ")
#     value = input("Enter Your Favourite Language: ")
#     d.update({key:value})
# print(d)
# If two names are same it will display the latest entered favourite language.
# 7. Write a program to find out whether a given post is talking about “Harry” or not.
# content = "Harry Is An Excellent Coder"
# if  "Harry" in content:
#     print("Yes! The Given Post Is Talking About Harry")
# else:
#     print("No! The Given Post Is Not Talking About Harry")

# 7. Write a program to print the following star pattern.
# *
# ***
# ***** for n = 3
# print(" ", end = "")
# print("*",end = "")
# print(" ")
# print("",end = "")
# print("*"*3)
# print("*"*5)

# 7. Write a python function to remove a given word from a list ad strip it at the same
# time
# def removenstrip(r):
#     if r in l:
#         l.remove(r)
#         str(r)
#         r.strip()
# l = [1," Hi","Hello",5,6,"Doraemon"]
# r = input("Enter The Word To Remove: ")
# removenstrip(r)
# print(l)

# 7. Write a program to find out the line number where python is present from ques 6.
# with open("/home/arshad/Muskan/word.txt") as f:
#     content = f.readlines()
#     lineno = 1
#     for line in content:
#         if 'python' in line:
#             print(f"Yes python present in file in line no.{lineno}")
#         lineno += 1
# 7.
# 7. Override the __len__() method on vector of problem 5 to display the dimension of the
# vector.
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
    
#     def __len__(self):
#         return len(self.__dict__)
    
# v = Vector(1,2,3)
# v2 = Vector(4,5,6)
# print(f"The Dimensions Are {len(v+v2)}")
# print("The Sum Of The Two Vectors Is: ",v+v2)
# print("The Dot Product Of The Two Vectors Is: ",v*v2)

# 7. Explore the ‘Flask’ module and create a web server using Flask & Python.
# import os

# from flask import Flask


# def create_app(test_config=None):
#     # create and configure the app
#     app = Flask(__name__, instance_relative_config=True)
#     app.config.from_mapping(
#         SECRET_KEY='dev',
#         DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
#     )

#     if test_config is None:
#         # load the instance config, if it exists, when not testing
#         app.config.from_pyfile('config.py', silent=True)
#     else:
#         # load the test config if passed in
#         app.config.from_mapping(test_config)

#     # ensure the instance folder exists
#     os.makedirs(app.instance_path, exist_ok=True)

#     # a simple page that says hello
#     @app.route('/hello')
#     def hello():
#         return 'Hello, World!'

#     return app