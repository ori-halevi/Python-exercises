"""
כתבו תוכנית הקולטת מהמשתמש סדרה של מספרים שלמים אי- שליליים המסתיימת ב -)-1(.
בסוף הקליטה עליכם להציג:
- המספר המקסימלי
- המספר המינימלי
- ממוצע המספרים
- כמות המספרים
- כמות המספרים הזוגיים
- כמו המספרים האי זוגיים
אם הסדרה ריקה יש להודיע על כך
"""
ori_list = []
ori_list.append(input("Enter a number: "))
while not int(ori_list[-1]) == -1:
    ori_list.append(input("Enter a number: "))
ori_list.pop()

biggest = int(ori_list[0])
smallest = int(ori_list[0])

for i in ori_list:
    if int(i) > biggest:
        biggest = int(i)
print("biggest:", biggest)

for i in ori_list:
    if int(i) < smallest:
        smallest = int(i)
print("smallest:", smallest)

sum_ = 0
for i in ori_list:
    sum_ = int(sum_) + int(i)
print("The average is:", sum_ / 2)




