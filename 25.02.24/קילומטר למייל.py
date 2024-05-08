def is_valid(value):
    if (isinstance(value, float) or isinstance(value, int)) and value > 0:
        return True
def convert_to_mile(kilometer: float):
    if is_valid(kilometer):
        mile = 0.621371192
        result = kilometer * mile
        return result
    else:
        return "Not valid distance"

mile = convert_to_mile(8.4)
print(mile)
