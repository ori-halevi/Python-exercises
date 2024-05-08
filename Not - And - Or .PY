grade = "B"
score = 80
is_passing = grade == 'A' or (grade == 'B' and score >= 70)
is_excellent = grade == 'A' and score >= 90
print(is_passing and not is_excellent)
print(not is_excellent)
print(is_passing)
