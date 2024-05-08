"""
in this project i considers 0 as negative.
"""
num1 = input("Please type your first number: ")
num2 = input("Please type your second number: ")
num3 = input("Please type your third number: ")
num4 = input("Please type your fourth number: ")
num5 = input("Please type your fifth number: ")
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
num4 = int(num4)
num5 = int(num5)


# Calculate the average:
average = (num1 + num2 + num3 + num4 + num5) / 5
print("The average is:")
print(average)
print()


# Check if the numbers are even or odd:
if not num1 % 2:
    even_or_odd = "even"
else:
    even_or_odd = "odd"
print("the number:", num1, "it's:", even_or_odd)

if not num2 % 2:
    even_or_odd = "even"
else:
    even_or_odd = "odd"
print("the number:", num2, "it's:", even_or_odd)

if not num3 % 2:
    even_or_odd = "even"
else:
    even_or_odd = "odd"
print("the number:", num3, "it's:", even_or_odd)

if not num4 % 2:
    even_or_odd = "even"
else:
    even_or_odd = "odd"
print("the number:", num4, "it's:", even_or_odd)

if not num5 % 2:
    even_or_odd = "even"
else:
    even_or_odd = "odd"
print("the number:", num5, "it's:", even_or_odd)

print()

# Chack if the numbers are positive
if num1 > 0:
    negative_or_positive = "positive"
else:
    negative_or_positive = "negative"
print("the number:", num1, "it's:", negative_or_positive)

if num2 > 0:
    negative_or_positive = "positive"
else:
    negative_or_positive = "negative"
print("the number:", num2, "it's:", negative_or_positive)

if num3 > 0:
    negative_or_positive = "positive"
else:
    negative_or_positive = "negative"
print("the number:", num3, "it's:", negative_or_positive)

if num4 > 0:
    negative_or_positive = "positive"
else:
    negative_or_positive = "negative"
print("the number:", num4, "it's:", negative_or_positive)

if num5 > 0:
    negative_or_positive = "positive"
else:
    negative_or_positive = "negative"
print("the number:", num5, "it's:", negative_or_positive)