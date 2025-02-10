# Create a Python program to convert temperatures between Celsius and Fahrenheit.

# Input: A temperature value (can be in either Celsius or Fahrenheit).
# Output: Convert and display the temperature in the other unit.
# Hints: Use basic arithmetic formulas for conversion (C = (F - 32) * 5/9 and F = C * 9/5 + 32).

option= """1) Convert Celsius to Fahrenheit
2)Convert Fahrenheit to Celsius  """
print (option)
X = float(input("Enter Your Choice"))
if X == 1:
    celsius = float(input("Enter the temperature in Celsius: "))
    Celsius = (celsius * 1.8) + 32
    print("Temperature in Fahrenheit is: ", Celsius)
else:
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    Fahrenheit = (fahrenheit - 32) * 5 / 9
    print("Temperature in Celsius is: ", Fahrenheit)

# 2) Strings and String Operations (Palindrome Check)
word = input("Enter a word: ")

reversed_word = word[::-1]

if word == reversed_word:
    print("Palindrome")
else:
    print("Not Palindrome")

# 3. Lists (Find Largest Number)
numbers = [2, 3, 1, 4, 9]
largest = max(numbers)
print(f"Largest number: {largest}")

# 4. Tuples (Swap First and Last
def swap_tuple_elements(tup):
    return (tup[-1], *tup[1:-1], tup[0])

tup = (1, 2, 3, 4)
swapped_tup = swap_tuple_elements(tup)
print(f"Swapped tuple: {swapped_tup}")

# 5. Dictionaries (Word Frequency)
sentence = input("Enter a sentence: ").split()
word_count = {word: sentence.count(word) for word in set(sentence)}
print(f"Word frequency: {word_count}")

#  6. Sets (Intersection of Two Sets)
set1 = {1, 2, 3}
set2 = {2, 3, 4}
intersection = set1 & set2
print(f"Intersection: {intersection}")

#  7. If/Else Statements (Positive, Negative, or Zero)
number = float(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

# 8. Loops (Sum of Even Numbers)
n = int(input("Enter a number: "))
sum_even = sum(i for i in range(1, n+1) if i % 2 == 0)
print(f"Sum of even numbers: {sum_even}")

#   9) Functions (Average of List)
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

numbers = [2, 4, 6, 8, 10]
average = calculate_average(numbers)
print(f"Average: {average}")

#  10. List Comprehension (Squares of Numbers)
squares = [x**2 for x in range(1, 11)]
print(f"Squares: {squares}")

#  11. Lambda Functions (Sort Tuples by Second Element)
tuples = [(1, 2), (3, 1), (5, 4)]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(f"Sorted tuples: {sorted_tuples}")

# 12. Exception Handling (Division by Zero)
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# 13. File Handling (Count Lines and Words)
with open("sample.txt", "r") as file:
    lines = file.readlines()
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)

print(f"Lines: {num_lines}, Words: {num_words}")

# 14. Classes and Objects (Car Class)
class Car:
    def _init_(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

    def car_age(self):
        return 2025 - self.year

my_car = Car("Toyota", "Camry", 2015)
my_car.display_info()
print(f"Car age: {my_car.car_age()} years")

# 15. Modules and Libraries (Factorial Using Math)
import math

n = int(input("Enter a number: "))
factorial = math.factorial(n)
print(f"Factorial: {factorial}")

# 16. Recursion (Factorial Using Recursion)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter a number: "))
print(f"Factorial: {factorial(n)}")

# 17. Regular Expressions (Email Validation)
import re

email = input("Enter an email address: ")
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")
 
#  18. Working with Dates and Times (Current Date and Time)
    import datetime

current_datetime = datetime.datetime.now()
print(f"Current date and time: {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}")

# 19. Decorators (Measure Execution Time)
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

@measure_time
def slow_function():
    time.sleep(2)

slow_function()

# 20. Web Scraping (Scraping Article Titles)
import requests
from bs4 import BeautifulSoup

url = input("Enter the URL: ")
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

titles = [article.get_text() for article in soup.find_all('h2')]  # Assuming titles are in <h2> tags
print("Article Titles:")
for title in titles:
    print(title)