valid_inputs = ("W", "V", "S")
reports = {}
work_days = vacation = sick = 0
for i in range(20):
    worker_input = input("Did you went to work today? [W/V/S]: ")
    while worker_input not in valid_inputs:
        worker_input = input("Please enter a valid input! [W/V/S]: ")
    day = i + 1
    reports[f"day {day}"] = worker_input

for element in reports.values():
    if element == "W":
        work_days += 1
    elif element == "V":
        vacation += 1
    elif element == "S":
        sick += 1
    else:
        print("Something went wrong!")
        break

print(f"Work: {work_days}, Sick: {sick}, Vacation: {vacation}")

