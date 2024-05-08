def palindrome(a):
    if len(a) > 1:
        print(a[0], end=" ")
        palindrome(a[1:])
    elif len(a) == 1:
        print(a[0], end=" ")
    print(a[0], end=" ")

my_array = [20, 40, 60, 80, 100]
palindrome(my_array)

print()
def palindrome2(a2):
    if len(a2) == 0:
        return
    print(a2[0], end=" ")
    palindrome2(a2[1:])
    print(a2[0], end=" ")

palindrome2([20, 40, 60, 80, 100])