# 10 MARKS QUESTIONS...
# 1. Write a python program to check whether the string is Palindrome or not.
s = input("Enter a string: ")
if s == s[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

# 2. Write a Python Program to Check accepted number is Prime or not.
n = int(input("Enter A Number: "))
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count += 1
if count == 2:
     print("The number is prime.")
else:
    print("The number is not prime.")

# 3.Write a Python program to convert a list to a tuple.
l = [2,5,"a",89]
t = tuple(l)
print(type(t))

# 4. Write a Python Program to Check Armstrong Number.
n = int(input("Enter A Number: "))
order = len(str(n))
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if n == sum:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")

# 5.Write a Python Program to Check whether the year is Leap Year or Not.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year,"is not a leap year.")

# 6.Write a Python function to accept Three numbers and find the Minimum of them.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
def find_min(a, b, c):
    if a < b and a < c:
        return a
    elif b  <  a and b < c:
        return b
    else:
        return c
min_num = find_min(a, b, c)
print("The minimum number is:", min_num)

# 7. Write a Python Program to Square Each Element of the List and Print List in Reverse
# Order.
l = [2,5,4,7,6]
squared_list = [x**2 for x in l]
reversed_list = squared_list[::-1]
print("Squared list in reverse order: ",reversed_list)

# 8.Write a Python program to split a list into two lists: One containing positive numbers and
# another containing negative numbers.
l = [2,-9,-5,-7,8,7]
pos = []
neg = []
for i in l:
    if i >= 0:
        pos.append(i)
    else:
        neg.append(i)
print("Original list: ",l)
print("Positive list: ",pos)
print("Negative list: ",neg)

# 9. Write a Python program to remove duplicates from a list.
l = [2,5,4,7,6,2,5]
unique_list = list(set(l))
print("Original list: ",l)
print("List after removing duplicates: ",unique_list)

# 10.Write a python program to perform arithmetic operations (+, -, *, /, %).
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition: ",a+b)
print("Subtraction: ",a-b)
print("Multiplication: ",a*b)
print("Division: ",a/b)
print("Modulus: ",a%b)  

# 11. Write a python program to find the frequency of characters in a string.
s = input("Enter a string: ")
frequency = {}
for char in s:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print("Frequency of characters in the string: ",frequency)

# 12. Write a Python Program to Check if a Number is Odd or Even.
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# 13. Write a Python program to sum all the items in a list.
l = [2,5,4,7,6]
total = sum(l)
print("The sum of all the items in the list: ",total)

# 14. Write a Python program to get the 4th element from front and 6th element from last of a
# tuple.
t = (2,5,"a",89,7,6,4,3,8)
print("4th element from front: ",t[3])
print("6th element from last: ",t[-6])

# 15. Write a Python Program to Find the Factorial of a Number.
n = int(input("Enter a number: "))
fact = 1
for i in range(1,n+1):
    fact *= i
print(f"Factorial of {n} is: {fact}")

# 16. Write a Python program to find maximum and the minimum value in a set.
s = {2,5,4,7,6}
max_s = max(s)
min_s = min(s)
print("Maximum value in the set: ",max_s)
print("Minimum value in the set: ",min_s)

# 17.Write a Python Program to Calculate the Area of a Rectangle and Circle.
l = int(input("Enter the length of the rectangle: "))
b = int(input("Enter the breadth of the rectangle: "))
r = int(input("Enter the radius of the circle: "))
print("Area of the rectangle: ",l*b)
print("Area of the circle: ",3.14*r*r)

#18. Python Program to Swap Two Numbers
a = int(input("enter the first number: "))
b = int(input("Enter the second number: "))
print("Numbers before swapping: ",a,b)
print("Swapping Numbers...")
s = a
a = b
b = s
print("Numbers after swapping: ",a,b)

# 19.Write a Python program to define a function that counts the number of digits in a given
# number.
def count_digits(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count
num = int(input("Enter a number: "))
print("Number of digits in the number: ",count_digits(num))

# 20.Write a Python Program to Calculate the Sum and Average of Numbers in a Given List.
l = [2,6,4,8,9]
total = sum(l)
avg = total / len(l)
print("Sum of the numbers in the list: ",total)
print("Average of the numbers in the list: ",avg)

# 21. Write a Python program to find the Maximum of three numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
    print("The maximum number is: ",a)
elif b > a and b > c:
    print("The maximum number is: ",b)
else:
    print("The maximum number is: ",c)

# 22. Write a python program to replace special symbol in string with # character.
s = input("Enter a string: ")
updated_string = ''.join('#' if not c.isalnum() else c for c in s)
print("Updated string after replacing special symbols with #: ",updated_string)

# 23. Write a Python program to get the largest and smallest number from a list.
l = [2,5,4,7,6]
largest = max(l)
smallest = min(l)
print("Largest number in the list: ",largest)
print("Smallest number in the list: ",smallest)

# 24. Write a Python Program to Interchange First and Last Elements of in a List.
l = [2,5,4,7,6]
l[0], l[-1] = l[-1], l[0]
print("List after interchanging first and last elements: ",l)

# 25. Write a python program to Reverse words in a given String.
s = input("Enter a string: ")
reversed_string = ' '.join(reversed(s.split()))
print("Reversed string: ",reversed_string)

# 26. Write a python program to arrange string characters such that lowercase letters should
# come first.
s = input("Enter a string: ")
lowercase = ''.join(c for c in s if c.islower())
uppercase = ''.join(c for c in s if c.isupper())
arranged_string = lowercase + uppercase
print("String with lowercase letters first: ",arranged_string)

# 27. Write a Python Program to Check if a Number is Positive, Negative or Zero.
n = int(input("Enter a number: "))
if n > 0:
    print("The number is positive.")
elif n < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# 28. Write a Python program to find the length of a tuple.
t = (2,5,"a",89)
print("Length of the tuple is: ",len(t))

# 29. Write a Python program to merge two Python dictionaries.
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d1.update(d2)
print("Merged dictionary: ",d1)

# 20 MARKS QUESTIONS...
# 1. Write a Python program to accept a list and separate even and odd elements.
l = [4,6,2,8,7,9,3,1,5]
eve = []
odd = []
for i in l:
    if i % 2 == 0:
        eve.append(i)
    else:
        odd.append(i)
print("Even Number List: ",eve)
print("Odd Number List: ",odd)
# 2. Write a Python program to find the length of a set.
s = {2,5,4,7,6}
count = 0
for i in s:
    count += 1
print("Length of the set: ",count)

# 3. Write a Python program to sort (ascending and descending) a dictionary by value.
d = {"a": 3, "b": 1, "c": 2,'d':4,'e':5}
print("Dictionary sorted in ascending order by value: ",sorted(d.items(), key=lambda x: x[1]))
print("Dictionary sorted in descending order by value: ",sorted(d.items(), key=lambda x: x[1], reverse=True))

# 4. Write a Python program to find the repeated items of a tuple and remove repeated items
# of a tuple and display updated tuple.
t = (2,5,"a",89,2,5)
repeated = set()
uni = set()
for i in t:
    if i in uni:
        repeated.add(i)
    else:
        uni.add(i)
print("Repeated items in the tuple: ",repeated)
updated_tuple = tuple(uni)
print("Updated tuple after removing repeated items: ",updated_tuple)

# 5. Write a Python program to check whether a string starts with a capital letter, ends with a
# digit and contains at least one special character.

s = input("Enter a string: ")
if s[0].isupper() and s[-1].isdigit() and any(not c.isalnum() for c in s):
    print("The string starts with a capital letter, ends with a digit and contains at least one special character.")
else:
    print("The string does not meet the specified conditions.")

# 6. Write a Python program to Display multiplication table of a number.
n = int(input("Enter A Number: "))
for i in range(1,11):
    print(f"{n} X {i} = {n*i}")

# 7. Write a Python function to check number in range.
n = int(input("Enter A Number: "))
def check_range(num):
    if 1 <= num <= 100:
        return "The number is in the range."
    else:
        return "The number is out of range."
print(check_range(n))

# 8. Write a Python function that accepts a string and calculate the number of vowels and
# consonants.
s = input("Enter A String: ")
vowels = 0
consonants = 0

for i in s:
    if i in 'aeiouAEIOU':
        vowels += 1
    else:
        consonants += 1
print(f"Number Of Vowels in the string: {vowels}, and number of consonants in string: {consonants}")


# 9. Write a Python Program to Print the pattern as below: *, * *, * * *.
n = 3
for i in range(1,n+1):
    print('*'*i)

# 10. Write a Python program to accept marks of 3 subjects and calculate total, average and
# grade.
s1 = int(input("Enter marks of subject 1: "))
s2 = int(input("Enter marks of subject 2: "))
s3 = int(input("Enter marks of subject 3: "))
total = s1+s2+s3
average = total/3
if total >= 90:
    grade = 'A'
elif total >= 50:
    grade = 'B'
else:
    grade = 'C'
print(f"Total Marks: {total}, Average Marks: {average}, Grade: {grade}")

# 11. Write a Python program to create dictionary from string.
s = input("Enter a string: ")
d = {char: s.count(char) for char in set(s)}
print("Dictionary created from the string: ",d)

# 12. Write a Python program to remove duplicate characters and replace spaces with
# underscore.
s = input("Enter A String: ")
ss = set(s)
updated_string = ''.join(ss).replace(' ', '_')
print("Updated string after removing duplicate characters and replacing spaces with underscore: ",updated_string)

# 13. Write a Python program to find symmetric difference of two sets.
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print("Symmetric difference: ", s1^s2)

# 14. Write a Python Program to Remove All Occurrences of an Element from a Given List.
l = [2,5,4,7,6,8,9,2,5,7,9]
el = int(input("Enter the element to remove: "))
for i in l:
    if i == el:
        l.remove(i)
print("Updated list after removing all occurrences of the element: ",l)

# 15. Write a Python program to copy elements from tuple.
t1 = (2,5,"a",89)
t2 = tuple(t1)
print("Copied tuple: ",t2)

# 16. Write a Python program to combine two dictionaries adding values for common keys.
# d1 = {"a": 1, "b": 2, "c": 3}
# d2 = {"b": 3, "c": 4, "d": 5}
# combined_dict = {key: d1.get(key, 0) + d2.get(key, 0) for key in set(d1) | set(d2)}
# print("Combined dictionary: ",combined_dict)

# 17. Write a Python program to print all odd numbers between 1 and 50 using a while loop.
l = set()
i = 1
while i <= 50:
    if i % 2 != 0:
        l.add(i)
    i += 1
print("Odd numbers between 1 and 50: ",l)

# 18. Write a Python program to accept a sentence and Display total number of words and
# each word with its starting index.
s = input("Enter a sentence: ")
words = s.split()
print("Total number of words: ",len(words))
for i, word in enumerate(words):
    print(f"Word: {word}, Starting Index: {s.index(word)}")

# 19. Write a Python program to concatenate dictionaries.
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
concatenated_dict = d1.update(d2)
print("Concatenated dictionary: ",d1)

# 20. Write a python program to find word in string which contains both digit and number.
s = input("Enter a string: ")
words = s.split()
result = []
for word in words:
    if any(c.isdigit() for c in word) and any(c.isalpha() for c in word):
        result.append(word)
print("Words that contain both digits and letters: ",result)

# 21. Write a Python program to Accept Three Numbers and find Minimum and Maximum of
# these Numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Maximum number is: ",max(a,b,c))
print("Minimum number is: ",min(a,b,c))

# 22. Write a Python program to count items in dictionary without len().
d = {"a": 1, "b": 2, "c": 3,'d':4,'e':5}
count = 0
for key in d:
    count += 1
print("Number of items in the dictionary: ",count)

# 23. Write a python program to convert decimal to binary using function.
# n = int(input("Enter a decimal number: "))
# def decimal_to_binary(num):
#     binary = ''
#     while num > 0:
#         binary = str(num % 2) + binary
#         num //= 2
#     return binary
# binary_number = decimal_to_binary(n)
# print(f"Binary representation of {n} is: {binary_number}")

# 24. Write a Python program to convert tuple to string and reverse.
t = (2,5,"a",89)
s = ' '.join(map(str, t))
reversed_s = s[::-1]
print("Tuple converted to string: ",s)
print("Reversed string: ",reversed_s)

# 25. Write a Python program to generate dictionary (x, x*x).
d = {x:x*x for x in range(1,16)}
print("Generated dictionary: ",d)

# 26. Write a Python program to get the maximum and minimum value in a dictionary.
d = {"a": 3, "b": 1, "c": 2,'d':4,'e':5}
max_d = max(d.values())
min_d = min(d.values())
print("Maximum value in the dictionary: ",max_d)
print("Minimum value in the dictionary: ",min_d)

# 27. Write a Python program to create a dictionary of keys x, y, and z where each key has as
# value a list from 11-20, 21-30, and 31-40 respectively. Access the fifth value of each key
# from the dictionary.
x = list(range(11, 21))
y = list(range(21, 31))
z = list(range(31, 41))
d = {'x': x, 'y': y, 'z': z}
print("Fifth value of key 'x': ",d['x'][4])
print("Fifth value of key 'y': ",d['y'][4])
print("Fifth value of key 'z': ",d['z'][4])

# 28. Write a python program to sort the tuple.
# t = (2,5,"a",89,7,6)
# print("Original tuple: ",t)
# sorted_tuple = tuple(sorted(t, key=lambda x: (isinstance(x, str), x)))
# print("Sorted tuple: ",sorted_tuple)

# 29. Write a Python function that accepts a string and calculate the number of upper case
# letters and lower case letters.
s = input("Enter A String: ")
upper = 0
lower = 0
for i in s:
    if i.isupper():
        upper += 1
    elif i .islower():
        lower += 1
print(f"Number of upper case letters: {upper}, and number of lower case letters: {lower}")

# 30. Write a Python program to reverse sentence word order.
s = input("Enter a sentence: ")
words = s.split()
reversed_sentence = ' '.join(reversed(words))
print("Reversed sentence: ",reversed_sentence)

# 31. Write a Python program to Remove duplicate characters and Vowels from a string and
# display the modified string.
s = input("Enter A String: ")
vowels = 'aeiouAEIOU'
sl = []
for i in s:
    if i in s and i in vowels:
        s = s.replace(i,'')
        
# print("Updated string after removing duplicate characters and vowels: ",s)

# 32. Write a Python program to create list of tuples (number, square).
tuples_list = []
for i in range(1,21):
    t = (i, i*i)
    tuples_list.append(t)
print("List of tuples (number, square): ",tuples_list)

# 33. Write a Python program to accept two strings and Check whether both strings are equal
# or not. Display appropriate message (without using ==).

a = input("Enter The First String: ")
b = input("Enter The Second String: ")
if a.__eq__(b):
    print("Both strings are equal.")
else:
    print("Both strings are not equal.")

# 34. Write a Python program to mask a string such that first and last characters remain same
# and all middle characters are replaced by *.
s = "Hi I Am Muskan"
s1 = ' '.join(s[0] + '*' * (len(s) - 2) + s[-1])
print("Masked string: ",s1)
    
# 35. Write a Python program to accept two numbers and perform Bitwise AND, OR, NOT and
# XOR operations on them.
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print("Bitwise AND: ",n1 & n2)
print("Bitwise OR: ",n1 | n2)
print("Bitwise NOT of first number: ",~n1)
print("Bitwise NOT of second number: ",~n2)
print("Bitwise XOR: ",n1 ^ n2)

# 36. Write a Python program to partition list into negative, zero and positive.
l = [1,6,-8,-9,7,-5,0,4,-6,6,-3,7,0]
p = []
n = []
z = []
for i in l:
    if i > 0:
        p.append(i)
    elif i < 0:
        n.append(i)
    else:
        z.append(i)
print("Positive numbers: ",p)
print("Negative numbers: ",n)
print("Zeroes: ",z)

# 37. Write a Python program to check whether an element exists within a tuple.
t = (2,5,"a",89)
el = input("Enter an element to check: ")
if el in t:
    print("The element exists in the tuple.")
else:
    print("The element does not exist in the tuple.")

# 38. Write a Python function to print sum of all numbers in list.
l = [2,5,4,7,6]
def sum_of_list(lst):
    return sum(lst)
print("Sum of all numbers in the list: ",sum_of_list(l))    

# 39. Write a Python program to create union and intersection of sets.
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
union = s1 | s2
intersection = s1 & s2
print("Union of sets: ",union)
print("Intersection of sets: ",intersection)

# 40. Write a Python program to remove all even numbers from a list.
l = [1,6,8,9,7,5,4,6,3,7]
for i in l:
    if i % 2 == 0:
            l.remove(i)
print("List after removing all even numbers: ",l)

# 41. Write a Python program to find largest, smallest, sum and average of list.
l = [2,3,6,7,4,9,66,23,54,90,76]
lar = max(l)
sma = min(l)
tot = sum(l)
ave = tot/len(l)
print("Largest number in the list: ",lar)
print("Smallest number in the list: ",sma)
print("Sum of the numbers in the list: ",sum(l))
print("Average of the numbers in the list: ",ave)

# 42. Write a python program to convert lowercase to uppercase and vice versa.
s = input("Enter A String: ")
converted_string = ''
for i in s:
    if i.islower():
        converted_string += i.upper()
    elif i.isupper():
        converted_string += i.lower()
    else:
        converted_string += i
print("Converted string: ",converted_string)

# 43. Write a Python program to accept two strings and find common characters and check
# equality.
s = input("Enter the first string: ")
t = input("Enter the second string: ")
common_characters = set(s) & set(t)
print("Common characters: ",common_characters)
if s.__eq__(t):
    print("Both strings are equal.")
else:
    print("Both strings are not equal.")

# 44. Write a Python program to check whether a given number is divisible by 5 and 7 and
# also check even or odd.
n = int(input("Enter a number: "))
if n % 5 == 0 and n % 7 == 0:
    print("The number is divisible by both 5 and 7.")
else:
    print("The number is not divisible by both 5 and 7.")
if n % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# 45. Write a Python function to check perfect number.
n = int(input("Enter a number: "))
def is_perfect(num):
    if num < 1:
        return False
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num
if is_perfect(n):
    print("The number is a perfect number.")
else:
    print("The number is not a perfect number.")    

# 46. Write a Python program to print all prime numbers in a range.
count = 0
pr = []
for i in range(1,101):
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        pr.append(i)
    count = 0
print("Prime numbers between 1 and 100: ",pr)

# 47. Write a Python program to check prime using function.
n = int(input("Enter a number: "))
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
if is_prime(n):
    print("The number is prime.")
else:
    print("The number is not prime.")

# 48. Write a Python program to check substring presence.
s = "Hello, welcome to the world of Python programming!"
sub = input("Enter a substring to check: ")
if sub in s:
    print("The substring is present in the string.")
else:
    print("The substring is not present in the string.")

# 49. Write a Python program to count number of strings where string length is 3 or more and
# first and last character are same.
strings = ["abc", "xyz", "aba", "1221", "aa", "a"]
count = 0
for s in strings:
    if len(s) >= 3 and s[0] == s[-1]:
        count += 1
print("Number of strings where string length is 3 or more and first and last character are same: ",count)

# 50. Write a Python Program to Square Each Element of the List and Print List in Reverse
# Order.
l = [2,5,4,7,6]
squared_list = [x**2 for x in l]
reversed_list = squared_list[::-1]
print("Squared list in reverse order: ",reversed_list)

# 51. Write a program to find factorial using loop.
f = 1
n = int(input("Enter a number: "))
for i in range(1,n+1):
    f *= i
print(f"Factorial of {n} is: {f}")

# 52. Write a Python program to accept a sentence, count number of words and find longest
# and shortest word.
s = input("Enter a sentence: ")
words = s.split()
num_words = len(words)
longest_word = max(words, key=len)
shortest_word = min(words, key=len)
print(f"Number of words in the sentence: {num_words}")
print(f"Longest word: {longest_word}")
print(f"Shortest word: {shortest_word}")

# 53. Write a Python Program to Print Fibonacci sequence.
f1 = 0
f2 = 1
n = int(input("Enter the number of terms in Fibonacci sequence: "))
print("Fibonacci sequence: ", end="")
for i in range(n):
    print(f1, end=" ")
    f1, f2 = f2, f1 + f2


# 54. Write a Python program to find student with highest marks from dictionary.
d = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95, "Eve": 88}
highest_marks_student = max(d, key=d.get)
print(f"Student with the highest marks: {highest_marks_student} with marks {d[highest_marks_student]}")

# 55. Write a Python Program to Find the Sum of Natural Numbers.
n = int(input("Enter a number: "))
total = sum(range(1, n + 1))
print(f"The sum of the first {n} natural numbers is: {total}")

# 56. Write a Python Program to display whether a given number is Armstrong or not.
n = int(input("Enter a number: "))
order = len(str(n))
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if n == sum:
    print("The number is an Armstrong number.")     
else:
    print("The number is not an Armstrong number.")
