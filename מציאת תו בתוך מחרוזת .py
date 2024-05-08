def countletters(mainstring, letter):
    count = 0
    for i in mainstring:
        if i == letter:
            count += 1
    print("The letter", letter, "found", count, "times")

countletters("oriisthebest", "e")