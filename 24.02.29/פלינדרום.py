def palindrome_is(string):
    if string == string[::-1]:
        return True
    else:
        return False


user_input = input("Please enter a palindrome: ")
if palindrome_is(user_input):
    print(f"{user_input} is a palindrome!")
else:
    print(f"{user_input} it's not a palindrome!")
