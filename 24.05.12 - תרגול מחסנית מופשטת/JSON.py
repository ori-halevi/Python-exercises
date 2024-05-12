import json
# x = {"average" : 75, "max": 91}
# x["foo"] = "ggg"
# with open("data.json", "w") as f:
#     json.dump(x, f)


with open("data.json", "r") as f:
    x = json.load(f)

print(x)
