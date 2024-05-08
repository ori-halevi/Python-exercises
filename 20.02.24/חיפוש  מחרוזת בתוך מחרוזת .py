keyword = "ab"
big_sentence = "abcab"

start = 0
end = len(keyword)
count = 0

for i in range(len(big_sentence)):
    if keyword == big_sentence[start:end]:
        count += 1
    start += 1
    end += 1
print(count)
