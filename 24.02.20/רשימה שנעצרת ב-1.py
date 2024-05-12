"""
קלטו מספרים מהשתמש לתוך מערך עד שהמשתמש מכניס את המספר -1 . הדפיסו הודעה מתאימה אם
המערך ממויין בסדר עולה,
יורד או לא ממויין בכלל.
"""
not_uphill = False
not_downhill = False
mix_up = False
user_list = []
while -1 not in user_list:
    user_list.append(int(input("Fill this list whit one number each time: ")))
print("Your list:", user_list)

for i in range(len(user_list) - 1):
    if user_list[i] > user_list[i + 1]:
        not_uphill = True
    elif user_list[i] < user_list[i + 1]:
        not_downhill = True
    else:
        mix_up = True

if not_uphill and not_downhill:
    print("Mix up")
if not mix_up and not_uphill and not not_downhill:
    print("Downhill")
if not mix_up and not_downhill and not not_uphill:
    print("Uphill")
    