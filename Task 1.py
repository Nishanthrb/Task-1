# 1. Arithmetic Operations on Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition =", a + b)
print("Subtraction =", a - b)
print("Multiplication =", a * b)
print("Division =", a / b)
print("Modulus =", a % b)
print("Floor Division =", a // b)
print("Exponentiation =", a ** b)

# 2. Area and Perimeter of Rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
perimeter = 2 * (length + width)
print("Area =", area)
print("Perimeter =", perimeter)

# 2. Area and Perimeter of Square
side = float(input("Enter side: "))
area = side ** 2
perimeter = 4 * side
print("Area =", area)
print("Perimeter =", perimeter)

# 2. Area and Circumference of Circle
radius = float(input("Enter radius: "))
area = 3.14 * radius * radius
circumference = 2 * 3.14 * radius
print("Area =", area)
print("Circumference =", circumference)

# 3. Average of Three Numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
average = (a + b + c) / 3
print("Average =", average)

# 4. Comparison of Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Are equal?", a == b)
print("First number greater?", a > b)
print("First number less than or equal?", a <= b)

# 5. Square Root of a Number
import math
num = float(input("Enter a number: "))
print("Square Root =", math.sqrt(num))

# 6. Simple Interest and Compound Interest
principal = float(input("Enter Principal Amount: "))
rate = float(input("Enter Rate of Interest: "))
time = float(input("Enter Time in Years: "))
SI = (principal * rate * time) / 100
CI = principal * ((1 + rate / 100) ** time) - principal
print("Simple Interest =", SI)
print("Compound Interest =", CI)

# 7. Assignment Operators
x = 10
x += 5
print("After x += 5 :", x)
x -= 3
print("After x -= 3 :", x)
x *= 2
print("After x *= 2 :", x)
x /= 4
print("After x /= 4 :", x)
x %= 2
print("After x %= 2 :", x)
x *= 3
print("After x *= 3 :", x)

# 8. Swapping Two Numbers Using Arithmetic Operators
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a = a + b
b = a - b
a = a - b
print("After Swapping")
print("a =", a)
print("b =", b)

# 9. Cube Root of a Number

num = float(input("Enter a number: "))
cube_root = num ** (1/3)
print("Cube Root =", cube_root)

# 10. Find the Last 2 Digits of 8523
num = 8523
print("Last 2 Digits =", num % 100)

# 11. Remove the Last 2 Digits of 8523
num = 8523
print("Number after removing last 2 digits =", num // 100)
