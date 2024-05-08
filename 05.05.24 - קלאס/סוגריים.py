user_input = "(sd))(()"


def l(user_input):
    count = 0
    for i in user_input:
        if i == "(":
            count += 1
        if i == ")":
            count -= 1
        if count < 0:
            return False
    if count > 0:
        return False
    else:
        return True


print(l(user_input))

user_input_2 = "(jj[)]{}({)}"


def h(user_input_2):

