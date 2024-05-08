"""
כתבו תוכנית, הגדירו בה מערך בגודל זוגי כלשהו וקלטו אליו נתונים מהמשתמש. התוכנית תדפיס "כן" אם
המערך הינו "מערך מראה". אחרת, תדפיס "לא."
"""
happinesso_list = []

while len(happinesso_list) < 6:
    happinesso_list.append(input("First one in the per: "))
    happinesso_list.append(input("Second one in the per: "))
print("Your list:", happinesso_list)

happinesso_list_revers = happinesso_list[::-1]
for i in range(len(happinesso_list_revers)):
    happinesso_list_revers[i] = happinesso_list_revers[i][::-1]

is_a_mirror = True
for i in range(len(happinesso_list_revers)):
    if not happinesso_list[i] == happinesso_list_revers[i]:
        is_a_mirror = False
        break

if is_a_mirror:
    print("This is a mirror list!")
else:
    print("This is not a mirror list!")
