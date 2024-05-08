"""
ג. כתבו תוכנית הקולטת מהמשתמש שני מספרים טבעיים n ו - k.
התוכנית תדפיס n שורות, כאשר כל שורה מורכבת מ- k חלקים.
כל חלק מכיל n מספרים, ומסתיים בתו ’@‘.
בשורה ה- i כל חלק יכיל את המספרים: .
הערה: השורות ממוספרות מ-0 עד -n.1
לדוגמא עבור 5=n ו- 3=k, התוכנית תדפיס:
@ 4 3 2 1 0 @ 4 3 2 1 0 @ 4 3 2 1 0
@ 0 4 3 2 1 @ 0 4 3 2 1 @ 0 4 3 2 1
@ 1 0 4 3 2 @ 1 0 4 3 2 @ 1 0 4 3 2
@ 2 1 0 4 3 @ 2 1 0 4 3 @ 2 1 0 4 3
@ 3 2 1 0 4 @ 3 2 1 0 4 @ 3 2 1 0 4
− − + i i n i , 1, , 1, 0, 1, , 1
"""
rows_and_numbers = int(input("first num: "))
parts = int(input("second num: "))
start = 0

for e in range(rows_and_numbers):
    for y in range(parts):
        for i in range(rows_and_numbers)[start:]:
            print(i, end="")
        for g in range(start):
            print(g, end="")
        print("@", end="")
    start += 1
    print()
