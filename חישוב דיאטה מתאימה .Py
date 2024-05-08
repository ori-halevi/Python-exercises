age = input("Please enter your age: ")
weight = input("Please enter your weight: ")
height = input("Please enter your height: ")
age = int(age)
weight = int(weight)
height = int(height)
young = False
old = False
very_old = False

height_weight_relativity = weight / height
height_weight_relativity = int(height_weight_relativity)

if age > 11 and age < 20:
    young = True
elif age > 21 and age < 40:
    old = True
elif age > 41 and age < 120:
    very_old = True
else:
    print("age not valid!")
    exit()

if young and height_weight_relativity > 0.5 and height_weight_relativity < 2:
    print("Your recommended menu is the A-Menu")

elif young and height_weight_relativity > 2 and height_weight_relativity < 3.5:
    print("Your recommended menu is the B-Menu")

elif young and height_weight_relativity > 3.5 and height_weight_relativity < 5:
    print("Your recommended menu is the C-Menu")
else:
    print("You might be an elian...")