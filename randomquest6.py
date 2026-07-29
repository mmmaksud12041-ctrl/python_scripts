# # 6.
# # # 6. Write a python program to calculate the square of a number entered by the user.
sq = int(input("Enter The Number To Be Squared: "))
print("The Square Is: ",sq*sq)
# # 6.
# # 6.
# # 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
# # value and use key as their names. Assume that the names are unique
d = {}
for i in range(1,5):
    key = input("Enter Your Name: ")
    value = input("Enter Your Favourite Language: ")
    d.update({key:value})
print(d)

# # # 6. Write a program to calculate the grade of a student from his marks from the
# # # following scheme:
# # # 90 – 100 => Ex
# # # 80 – 90 => A
# # # 70 – 80 => B
# # # 60 – 70 =>C
# # # 50 – 60 => D
# # # <50
# # # => F

s = int(input("Enter Your Marks: "))
if (s > 90 and s <= 100):
    print("Grade: Excellent")
elif (s > 80 and s <= 90):
    print("Grade: A")
elif (s > 70 and s <= 80):
    print("Grade: B")
elif (s > 60 and s <= 70):
    print("Grade: C")
elif (s > 50 and s <= 60):
    print("Grade: D")
else:
    print("Grade: f")

# # # 6. Write a program to calculate the factorial of a given number using for loop.
f = int(input("Enter The Number: "))
fact = 1
for i in range(1,f+1):
    fact *= i
print("factorial= ",fact)

# # # 6. Write a python function which converts inches to cms
def inchestocms(inc):
    print("Centimeter = ",inc*2.54)
inchestocms(2)

# # # 6. Write a program to mine a log file and find out whether it contains ‘python’.
with open("/home/arshad/Muskan/word.txt") as f:
    content = f.read()

    if 'python' in content:
        print("Yes python present in file")
    else:
        ("No python not present in file")

# # # 6. Can you change the self-parameter inside a class to something else (say
# # # “harry”). Try changing self to “slf” or “harry” and see the effects.
class suming:
    def __init__(slf):
        pass

    def add(slf,a,b):
        slf.a = a
        slf.b = b
        print(a + b)
    
m = suming()
m.add(1,2)

# # 6. Write __str__() method to print the vector as follows:
# # 7i + 8j +10k

class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    
    def __str__(self):
        return f"{self.x}i + {self.y}y, + {self.z}z"
    
v = Vector(1,2,3)
v2 = Vector(4,5,6)
print("The Sum Of The Two Vectors Is: ",v+v2)

# 6. Run pip freeze for the system interpreter. Take the contents and create a similar
# virtualenv.
# Yes
