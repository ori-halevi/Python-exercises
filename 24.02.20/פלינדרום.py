"""
כתבו תוכנית הקולטת מספר טבעי ובודקת האם ספרותיו מהוות פלינדרום.
פלינדרום הוא ביטוי שיהיה זהה אם נקרא אותו מימין לשמאל וגם משמאל לימין.
דוגמה א':
קלט: 5073705
פלט: is palindrome 5073705
דוגמה ב':
קלט: 507375
פלט: is not palindrome 507375
"""
fun_integer = input("Please enter a number: ")
fun_integer_in_revers = fun_integer[::-1]

is_palindrome = True
for i in range(len(fun_integer)):
    if not fun_integer[i] == fun_integer_in_revers[i]:
        is_palindrome = False
        break
if is_palindrome:
    print("This is a palindrome!")
else:
    print("This is not a palindrome!")
