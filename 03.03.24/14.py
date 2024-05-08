def exponentiation(base: float | int, exponent: int) -> float:
    result = base
    for i in range(exponent - 1):
        result *= base
    return result


print(exponentiation(2.5, -2))
