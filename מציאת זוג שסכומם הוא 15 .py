"""
הקוד מדפיס את כל הזוגות של מספרים מתוך הרשימה allnumbers שבהם סכום המספרים בזוג הוא שווה למספר שהועבר כפרמטר onenum.
במקרה זה, הוא מדפיס את הזוגות (i, g) שעבורם i + g שווה ל־15.
"""


def splitto(all_numbers, one_num):
    for i in allnumbers:
        for g in all_numbers:
            if g + i == int(one_num):
                print(i, "and", g)


my_numa = [5, 9, 8, 7]
splitto(my_numa, 15)
