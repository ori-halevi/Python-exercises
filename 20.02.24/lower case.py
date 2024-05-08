"""
ב. כתבו תוכנית הקולטת מהמשתמש אות אנגלית קטנה ומדפיסה משולש אותיות באופן הבא:
בשורה הראשונה תופיע האות a , בשורה השנייה הרצף aba , בשורה השלישית הרצף abcba וכך הלאה
עד שבמרכז השורה האחרונה תופיע האות שנקלטה.
לדוגמא עבור הקלט d יודפס:
a
aba
abcba
abcdcba
"""
letter_user_input = ""
while letter_user_input != letter_user_input.lower() or len(letter_user_input) != 1:
    letter_user_input = input("Please enter a lower case letter: ")

all_letters = "abc"
for i in range(5):
    h = all_letters[:i]
    th = h[:-1] + h[::-1]
    if i == 4:
        print(h + letter_user_input + h[::-1])
    else:
        print(th)



