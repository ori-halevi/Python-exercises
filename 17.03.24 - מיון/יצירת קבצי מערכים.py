import random
trillion = []
for i in range(100000000):
    trillion.append(i)

with open("arry.txt", "w") as f:
    f.write(f"{trillion}")
