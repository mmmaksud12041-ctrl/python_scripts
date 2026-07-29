# # # 3. Install an external module and use it to perform an operation of your interest.
import math
num = int(input("Enter The Number: "))
print(math.sqrt(num))

# # # 3. Check the type of variable assigned using input () function.
var = input("Enter The Variable: ")
print(var,type(var))

# # # 3. Write a program to detect double space in a string.
str = input("Enter The String: ")
if ("  " in str):
    print("Double Space Detected ")
else:
    print("Double Space Not Detected ")

# # # 3. Check that a tuple type cannot be changed in python.
t = (12,65,True, 67)
t[0] = 76

# # # 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
s = {18,'18'}
print(s)
print("Yes,A Set Can Have 18 (int) And '18' (str) In It")

# # # 3. A spam comment is defined as a text containing following keywords:
# # # “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# # # to detect these spams.
spam1 = "Make a lot of money"
spam2 = "buy now"
spam3 = "subscribe this"
spam4 = "click this"
comm = input("Enter The Comment: ")
if (spam1 or spam2 or spam3 or spam4 in comm):
    print("This Is A Spam Comment")

# # # 3. Attempt problem 1 using while loop.
# # # Problem 1 : 1. Write a program to print multiplication table of a given number using for loop.
num = int(input("Enter The Number: "))
i = 1
while(i<=10):
    print(f"{num} X {i} = {num*i}")
    i += 1

# # # 3. How do you prevent a python print() function to print a new line at the end.
print("This Is How You Prevent A Python Print() Function To Print A New Line At The End." , end = "")
print("Do You All Got It")

# # # 3. Write a program to generate multiplication tables from 2 to 20 and write it to the
# # # different files. Place these files in a folder for a 13 – year old.
def generateTable(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}"

    with open(f"/home/arshad/Muskan/tables/table_{n}","w") as f:
        f.write(table)

for i in range(2,21):
    generateTable(i)

# # # 3. Create a class with a class attribute a; create an object from it and set ‘a’
# # # directly using ‘object.a = 0’. Does this change the class attribute?
class att:
    a = 0

object = att()
object.a = 9
print(att.a)
print(object.a)

# # 3. Create a class ‘Employee’ and add salary and increment properties to it.
class Employee: 
    salary = 20000
    increment = 20

    @property
    def salaryafterincrement(self):
        return ((self.salary*self.increment)/100)+self.salary
    
    @salaryafterincrement.setter
    def salaryafterincrement(self,salary):
        self.increment =  ((salary-self.salary)*100)/self.salary
    
e = Employee()
print(e.salaryafterincrement)
e.salaryafterincrement = 24000
print(e.increment)

# 3. Write a list comprehension to print a list which contains the multiplication table of a
# user entered number.
n = int(input("Enter The Number: "))
l = [n*i for i in range(1,11)]
print(l)

# 3. A list contains the multiplication table of 7. write a program to convert it to vertical
# string of same numbers.
l = [str(7*i) for i in range(1,11)]
vl = '\n'.join(l)
print(vl)
