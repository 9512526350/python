# 1. Loop Through a List
# Task: Iterate through a list and perform calculations.

# Instructions:
# Create a list of numbers: [10, 20, 30, 40, 50].
# Loop through the list and print each number multiplied by 2.
# Print the sum of all numbers in the list.
list =[10, 20, 30, 40, 50]

print(list)
for num in list:
    print(num * 2)

    print("sum is: ",sum(list))

# 2. List Comprehension
# Task: Create a filtered list using list comprehension.

# Instructions:
# Given a list of numbers [5, 12, 17, 24, 35], create a new list containing only numbers greater than 15.
# Square all the numbers in the new list using list comprehension.
# Print both the filtered and squared lists.

numbers = [5, 12, 17, 24, 35]
filtered_numbers = [num for num in numbers ]
print("Filtered num is : ",filtered_numbers)
squared_numbers = [num ** 2 for num in filtered_numbers]
print("squared num is :",squared_numbers)

# 3. The Syntax
# Task: Create and manipulate lists.

# Instructions:
# Create a list of strings: ["apple", "banana", "cherry", "date"].
# Add "orange" to the list using append().
# Insert "grape" at index 2 using insert().
# Remove "date" from the list.
# Print the final list.

fruit = ["apple", "banana", "cherry", "date"]
print(fruit)
fruit.append("orange")
print(fruit)
fruit.insert(2, "grape")
print(fruit)
fruit.remove("date")
print(fruit)

# 5. Sort List Alphanumerically
# Task: Sort a list of strings.

# Instructions:
# Create a list of names: ["Emma", "Olivia", "Liam", "Noah", "Sophia"].
# Sort the list alphabetically and print it.
# Sort the list in reverse alphabetical order and print it.
# Add "James" to the list, then sort again.

names = ["Emma", "Olivia", "Liam", "Noah", "Sophia"]
print("Original list: ",names)
names.sort()
print("Sorted list: ",names)
names.sort(reverse=True)
print("Sorted list in reverse: ",names)
names.append("James")
print("Sorted list after adding James: ",names)

# 6. Descending Order
# Task: Sort numbers and strings in descending order.

# Instructions:
# Given a list of numbers [50, 10, 70, 30, 90], sort it in descending order.
# Given a list of strings ["dog", "cat", "zebra", "elephant", "ant"], sort it in reverse alphabetical order.
# Print both sorted lists.
# numbers = [50, 10, 70, 30, 90]
# sorted_numbers = sorted(numbers, reverse=True)
# print("Sorted numbers: ",sorted_numbers)
# animal = ["dog", "cat", "zebra", "elephant", "ant"]
# sorted_strings = sorted(animal, reverse=True)
# print("Sorted strings: ",sorted_strings)

