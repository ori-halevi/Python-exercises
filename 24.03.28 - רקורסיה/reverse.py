def reverse(stri: str) -> str:
    if len(stri) == 0:
        return stri
    return stri[-1] + reverse(stri[:-1])

print(reverse("abcdef"))

