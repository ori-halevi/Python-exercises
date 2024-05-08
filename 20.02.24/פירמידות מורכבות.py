"""
כתבו תוכנית הקולטת מהמשתמש שני מספרים טבעיים n ו- k. התוכנית תדפיס n שורות.
כל שורה מורכבת מ- k חלקים. כל חלק מכיל n סימני $ ו- #, ומסתיים בתו ’@‘.
בשורות i האי-זוגיות (..,1,3,5) כל חלק (בגודל n) יתחיל ב- i סימני $ רצופים, ואחריהם בשאר
המקומות סימני #.
בשורות i הזוגיות (,2,4,6...) כל חלק (בגודל n) יתחיל ב- i סימני # רצופים, ואחריהם בשאר המקומות
סימני $.
הערה: השורות ממוספרות מ-1 עד n.
לדוגמא עבור 5=n ו- 3=k, התוכנית תדפיס:
(שים לב, יתכן והדוגמא מוצגת בהיפוך בגלל העורך שלך)
@ # # # # $ @ # # # # $ @ # # # # $
@ $ $ $ # # @ $ $ $ # # @ $ $ $ # #
@ # # $ $ $ @ # # $ $ $ @ # # $ $ $
@ $ # # # # @ $ # # # # @ $ # # # #
@ $ $ $ $ $ @ $ $ $ $ $ @ $ $ $ $ $
"""
rows_and_numbers = int(input("first num: "))
parts = int(input("second num: "))
start = 0

for i in range(rows_and_numbers):
    round = i +1
    if not round % 2 == 0:              # when the line number is odd
        for g in range(parts):
            for k in range(round):
                print("$ ", end="")
            for k in range(rows_and_numbers - round):
                print("# ", end="")
            
            print("@ ", end="")
    else:                           # when the line number is even
        for g in range(parts):
            for k in range(round):
                print("# ", end="")
            for k in range(rows_and_numbers - round):
                print("$ ", end="")
            print("@ ", end="")

    print()



