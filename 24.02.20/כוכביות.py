"""
א. כתבו תכנית הקולטת מספר טבעי, N, ומדפיסה מבנה כוכביות באופן הבא:
המבנה מורכב מחלק ימני וחלק שמאלי המכילים משולש כוכביות ומיושרים לצד ימין או שמאל בהתאם,
כאשר רק בשורה האחרונה אין רווח בין שני החלקים.
לדוגמא עבור 5=N יודפס המבנה הבא:
* * כוכבית אחת בכל חלק
** ** שתי כוכביות בכל חלק
*** *** שלוש כוכביות בכל חלק
**** **** ארבע כוכביות בכל חלק
********** חמש כוכביות בכל חלק
"""
user_num = -1
while user_num < 0:
    user_num = int(input("Please enter a number: "))
original_num = user_num

round = 1
while user_num > 1:
    for i in range(round):
        print("*", end="")
    print(" ", end="")
    for i in range(round):
        print("*", end="")
    round += 1
    user_num -= 1
    print()

for i in range(original_num * 2):
    print("*", end="")
