"""
כתוב תוכנית הקולטת מספר טבעי num וספרה k. התוכנית תדפיס את מספר הספרות בnum המתחלקות
ב-k ללא שארית.
"""
num = int(input("Please enter a number: "))
divider = float(input("Please enter a divider number: "))

for i in str(num):
    if not int(i) % divider:
        print(i)
