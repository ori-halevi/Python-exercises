def print_from_end(num):
    list_of_numbers = []
    for i in range(num):
        g = i + 1
        list_of_numbers.append(g)
    list_of_numbers = list_of_numbers[::-1]
    for i in list_of_numbers:
        print(i, end=" ")

if __name__ == "__main__":

    rounds = 5
    while rounds > 1:
        print_from_end(rounds)
        print()
        rounds -= 1
