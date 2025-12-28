from collections import Counter

# Ask the user for a string
s = input("Enter a string: ")
# Check palindrome
if s == s[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

# List of integers
numbers = [10, 20, 30, 40, 50]
# Calculate average
average = sum(numbers) / len(numbers)
print("Average:", average)

# Input first list
list1 = list(map(int, input("Enter elements of first list (space-separated): ").split()))
# Input second list
list2 = list(map(int, input("Enter elements of second list (space-separated): ").split()))
# Merge the lists
merged_list = list1 + list2
# Sort the merged list
merged_list.sort()
print("Merged and sorted list:", merged_list)

# Input tuples
tuple1 = tuple(map(int, input("Enter elements of first tuple (space-separated): ").split()))
tuple2 = tuple(map(int, input("Enter elements of second tuple (space-separated): ").split()))
# Merge tuples
merged_tuple = tuple1 + tuple2
# Sort the merged tuple
sorted_tuple = tuple(sorted(merged_tuple))
print("Merged and sorted tuple:", sorted_tuple)


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# Create tuple of even numbers
even_numbers = tuple(n for n in numbers if n % 2 == 0)
# Create tuple of odd numbers
odd_numbers = tuple(n for n in numbers if n % 2 != 0)
print("Even numbers tuple:", even_numbers)
print("Odd numbers tuple:", odd_numbers)

# Create empty dictionary
students = {}

while True:
    print("\nMENU")
    print("A - Add a student")
    print("B - Update marks")
    print("C - Search for a student")
    print("D - Display all students and marks")
    print("E - Exit")

    choice = input("Enter your choice: ").upper()

    if choice == 'A':
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks
        print("Student added successfully.")

    elif choice == 'B':
        name = input("Enter student name to update: ")
        if name in students:
            marks = int(input("Enter new marks: "))
            students[name] = marks
            print("Marks updated successfully.")
        else:
            print("Student not found.")

    elif choice == 'C':
        name = input("Enter student name to search: ")
        if name in students:
            print(f"{name}'s marks: {students[name]}")
        else:
            print("Student not found.")

    elif choice == 'D':
        if not students:
            print("No students in the dictionary.")
        else:
            print("Students and Marks:")
            for name, marks in students.items():
                print(name, ":", marks)

    elif choice == 'E':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")


words = ["apple", "banana", "kiwi", "cherry", "mango"]
# Create dictionary
word_length_dict = {word: len(word) for word in words}
print(word_length_dict)

# Take input from the user
text = input("Enter a string: ")
# Count spaces
spaces = text.count(" ")
print("Number of spaces in the string:", spaces)

def check_no_common_elements(list1, list2):
    common = set(list1).intersection(set(list2))
    if len(common) == 0:
        print("The two lists share NO common elements.")
    else:
        print("The two lists share common elements:", common)
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
check_no_common_elements(list1, list2)

# Example list
numbers = [1, 2, 2, 3, 4, 5, 1, 6, 2]
# Count occurrences
count = Counter(numbers)
# Print elements with count > 1
duplicates = [item for item, freq in count.items() if freq > 1]
print("Elements that appear more than once:", duplicates)

# Take input from the user
text = input("Enter a string: ")
# Get unique characters using a set
unique_chars = set(text)
# Print unique characters
print("Unique characters:", unique_chars)
# Print count of unique characters
print("Number of unique characters:", len(unique_chars))





