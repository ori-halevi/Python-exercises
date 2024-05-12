"""
הגדירו מערך וקלטו שני מספרים מהמשתמש לשני האיברים הראשונים במערך. התוכנית תמלא את איברי
המערך עד לאיבר העשירי )len המערכך יהיה 10( כך שערכו של כל איבר במקומות הזוגיים יהיה הסכום של
שני האיברים שלפניו וערכו של כל איבר במקומות האי זוגיים יהיה תוצאת המכפלה של שני האיברים לפניו.
"""
first_num = int(input("Please entre the first number: "))
second_num = int(input("Please enter the second number: "))
list_1 = [first_num, second_num]

while len(list_1) < 10:
    place = int(len(list_1))
    list_1.append(list_1[place - 1] * list_1[place - 2])
    list_1.append(list_1[place] + list_1[place - 1])

print(list_1)
