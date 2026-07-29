# # 4. Write a python program to print the contents of a directory using the os module.
# # # Search online for the function which does that.
import os
dir = '/home/arshad/Muskan'
print(os.listdir(dir))

# # # 4. Use comparison operator to find out whether ‘a’ given variable a is greater than
# # # ‘b’ or not. Take a = 34 and b = 80
a = 34
b = 80
if a>b:
    print("a is greater than b")
else:
    print("a is not greater than b")

# # # 4. Replace the double space from problem 3 with single spaces.
str = input("Enter The String: ")
if (" " in str):
    print("Single Space Detected ")
else:
    print("Single Space Not Detected ")

# # # 4. Write a program to sum a list with 4 numbers.
l = [24,56,78,98]
sum = 0
for i in l:
    sum += i
print("The Sum Of The List Is: ",sum)

# # # 4. What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?
print("The Length Of The Set S Is:",len(s))

# # # 4. Write a program to find whether a given username contains less than 10
# # # characters or not.
username = input("Enter The Username: ")
ch = input("Enter The Character To Be Checked: ")
if ch in username:
    print("The Character Is Present In The Username")
else:
    print("The Character Is Not Present In The Username")

# # # 4. Write a program to find whether a given number is prime or not.
num = int(input("Enter The Number: "))
if (num == 1):
    print("1 is neither prime nor composite")
elif num % 2 == 0:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

# # # 4. Write a recursive function to calculate the sum of first n natural numbers
def sum_naturals(n):
    sum = 0
    if n == 1:
        return 1
    else:
        for i in range(1,n+1):
            sum += i
    return sum
n = int(input("Enter The Number Of First Natural Numbers To Be Summed: "))
print("The Sum Of First",n,"Natural Numbers Is: ",sum_naturals(n))

# # # 4. A file contains a word “Donkey” multiple times. You need to write a program
# # # which replace this word with ##### by updating the same file.
with open('/home/arshad/Muskan/word.txt') as f:
    data = f.read()
    with open('/home/arshad/Muskan/word.txt', 'w') as f:
        data = data.replace('Donkey', '#####')
        f.write(data)

# # # 4. Add a static method in problem 2, to greet the user with hello.
class Calculator:
    @staticmethod
    def greet():
        print("Hello, Welcome To The Calculator Program!")  

    def __init__(self,n):
        self.n = n
    
    def square(self):
        return self.n ** 2

    def cube(self):
        return self.n * self.n * self.n
    def sqrt(self):
        return self.n ** 0.5

num = int(input("Enter The Number:"))
calc = Calculator(num)
print("Square Of The Number Is: ",calc.square())
print("Cube Of The Number Is: ",calc.cube())        
print("Square Root Of The Number Is: ",calc.sqrt())
Calculator.greet()
    
# # 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded
# # operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i

    def __add__(self,other):
        return Complex(self.r + other.r, self.i + other.i)
    
    def __mul__(self,other):
        real = self.r * other.r - self.i*other.i
        imag = self.r * other.i + other.r * self.i
        return(real,imag)
    def __str__(self):
        return f"{self.r} + {self.i}i"
    
c1 = Complex(3,4)
c2 = Complex(5,6)
print("The Sum Of The Complex Numbers Is: ",c1+c2)
print("The Product Of The Complex Numbers Is: ",c1*c2)

# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by
# handling the ‘ZeroDivisionError’.
try:
    a = int(input("Enter The Numerator: "))
    b = int(input("Enter The Denominator: "))
    print("The Result Of a/b Is: ",a/b)

# except ZeroDivisionError:
    if(b == 0):
        print("The Result Of a/b Is: Infinite")

# 4. Write a program to filter a list of numbers which are divisible by 5.
l = [54,76,77,45,90,23,56,100]
divby5 = lambda x: x % 5 == 0
filtered_list = list(filter(divby5, l))
print("Numbers Divisible By 5 Are: ",filtered_list)
