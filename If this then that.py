# This asks the user to a single character
char = input("Enter a single character: ")

# Changes the character to lowercase "A" and "a"
char = char.lower()

if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print("The character is a vowel.")
else:
    print("The character is not a vowel.")

#This program checks if the number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Ths program prints the day of the week based on the number entered by the user
day = int(input("Enter a number (1-7): "))

#Elif statements used to match the numbers to the days
if day == 1:
    print("The day is Monday.")
elif day == 2:
    print("The day is Tuesday.")
elif day == 3:
    print("The day is Wednesday.")
elif day == 4:
    print("The day is Thursday.")
elif day == 5:
    print("The day is Friday.")
elif day == 6:
    print("The day is Saturday.")
elif day == 7:
    print("The day is Sunday.")
else:
    print("Invalid input. Please enter a number between 1 and 7.")

# This program checks if the user is eligible to vote based on their age

#asks user to enter their age
age = int(input("Enter your age: "))

# Voting age is 18 but different in other countries
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# This program checks if a triangle is equalateral

# Asks user to enter the 3 sides
side1 = int(input("Enter 1 side: "))
side2 = int(input("Enter 2 side: "))
side3 = int(input("Enter 3 side: "))

# Checks if all sides are equal
if side1 == side2 == side3:
    print("The triangle is equilateral.")
else:
    print("The triangle is not equilateral.")

# This program finds the larger number bewteen two numbers

#Asks user to enter two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Compare's the two numbers 
if num1 > num2:
    print("The larger number is:", num1)
else:
    print("The larger number is:", num2)

# This program converts tempurature between celsius and fahrenheit

#celsius to fahrenheit conversion
c = int(input("Enter tempurature in celsius: "))

#Formaula for celsius to fahrenheit conversion
f = (c * 9/5) + 32
print("The temperature in fahrenheit is:", f)