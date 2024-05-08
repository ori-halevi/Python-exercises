
def ymf():
    global words
    # קבלת קלט מהמשתמש
    user_input = input("פקודתך: ")

    # חלוקת המחרוזת למילה הראשונה והשאר
    words = user_input.split(maxsplit=1)

    if len(words) > 1:
        first_word = words[0]
        rest_of_input = words[1]
    else:
        return Error()

    # הדפסת התוצאה
    if first_word == "קרא":
        if len(words) > 1:
            print(rest_of_input)
        else:
            print("")
    else:
        Error()

    ymf()

def Error():
    print(str(words) + " is not recognized as an internal or external command")
    ymf()

ymf()