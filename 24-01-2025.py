# 1) What is the result of this expression?
# result = 5 + 3 * 2 ** 3 // 4 % 3 - 1

result = '''the final Output is 
= 4'''
print(result)

# 2)  What is the result of this expression?
# a = 10
# b = 5
# result = a + b * 2

ans = '''ans is 20 
because b * 2 = 10 
and 10 +10 =20
ans:- 20'''
print (ans)

# 3) Convert Celsius to Fahrenheit OR Convert Fahrenheit to Celsius

option= """1) Convert Celsius to Fahrenheit
2)Convert Fahrenheit to Celsius  """
print (option)
X = float (input("Enter Your Choice"))
if X == 1:
    celsius = float(input("Enter the temperature in Celsius: "))
    Celsius = (celsius * 1.8) + 32
    print("Temperature in Fahrenheit is: ", Celsius)
else:
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    Fahrenheit = (fahrenheit - 32) * 5 / 9
    print("Temperature in Celsius is: ", Fahrenheit)

# Find the Maximum of Two Numbers using if else..
# a = 12
# b = 8

a =12
b = 8

if a > b:
    print("a is greater number")
else:
    print("b is greater number")