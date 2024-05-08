"""
כתוב תכנית הקולטת מספר שלם חיובי המייצג מספר תעודת זהות, ללא אפס מוביל וללא ספרת ביקורת.
התוכנית מחשבת ומדפיסה את מספר תעודת הזהות עם ספרת הביקורת.
חישוב ספרת הביקורת של תעודת זהות נעשה בשלושה שלבים:
.1 כופלים את הספרות השונות ב 2- וב1- לסירוגין:
הספרה האחרונה הימנית ביותר מוכפלת ב- .2
הספרה הלפני אחרונה השניה מימי מוכפלת ב - .1


הספרה שלפניה השלישית מימין מוכפלת ב- .2
וכן הלאה לסירוגין, עבור שאר הספרות (לא ידוע אם מספר הספרות זוגי או לא).
.2 סוכמים את סכום הספרות של המכפלות שהתקבלו.
לדוגמא: אם אחת המכפלות הינה 2*7=14 אז היא תורמת לסכום ,5 כי 5=4 + 1.
.3 מקבלים את ספרת הביקורת בתור המספר האי -שלילי הקטן ביותר שניתן להוסיף לתוצאת הסכום
שהתקבלה בשלב השני בכדי להגיע לכפולה של .10
לדוגמא: אם הסכום הכולל של ספרות הוא 24 הרי שספרת הביקורת היא ,6 כי 30 = 6 + 24 , ו - 30
הינו כפולה של 10 הקרובה ביותר ל - 24.

לדוגמא עבור ת"ז מס 56287 ספרת הביקורת היא ,6 כיוון ש:
ספרות תעודת הזהות: 7 8 2 6 5
הכופלים (לכל ספרה): 2 1 2 1 2
---------------------
המכפלות (לכל ספרה): 14 8 4 6 10
סיכום סכום הספרות: 24 = 1+0+6+4+8+1+4
ו6- הוא המספר האי שלילי הקטן ביותר אשר ניתן להוסיף לסכום 24 כדי להגיע לכפולה של .10
"""
id_num = str(input("Please enter your id: "))
id_revers = id_num[::-1]
first_numbers = []
second_numbers = []

for i in id_revers[::2]:
    first_numbers.append(str(int(i) * 2))
for i in id_revers[1::2]:
    second_numbers.append(i)
for i, e in enumerate(first_numbers):
    if len(e) > 1:
        first_numbers[i] = str(int(e[0]) + int(e[1]))

new_list = first_numbers + second_numbers
sum_ = 0
for i in new_list:
    sum_ = sum_ + int(i)

audit_num = 10 - int(str(sum_)[:0:-1])
audit_num = str(audit_num)[-1:]
print(audit_num)

