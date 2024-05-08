import os

def create_code():
    global code
    code = input("Please enter two numbers between 1 to 4: ")
    os.system('cls')
    if len(code) != 2:
        create_code()

def guss_again():
    global guss
    guss = input("Please enter your guss: ")
    if len(guss) != 2:
        guss_again()
    check_guss()

def check_guss():
    global guss, code
    if guss == code:
        print("good jub!")
    else:
        check_for_something()

def check_for_something():
    global guss, code
    if guss[0] == code[1] or guss[1] == code[0]:
        print("you were right about something!")
        guss_again()
    elif guss[0] == code[0] or guss[1] == code[1]:
        print("You half right!")
        guss_again()
    else:
        print("you lost")


create_code()
guss_again()
print("Press Enter to exit")
input()
