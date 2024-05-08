"""
כתבו תוכנית המקבלת מחרוזת ומחזירה את התו האמצעי שלה. אם המחרוזת באורך זוגי החזירו את שני
התווים.
"""

user_input = input("Please enter anything: ")

len = int(len(user_input))
lendevided = len // 2

if len % 2 == 0:
    print(user_input[lendevided - 1], user_input[lendevided])
else:
    print(user_input[lendevided])
