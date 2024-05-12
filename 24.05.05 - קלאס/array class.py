"""
Array needs to get capacity ahead!
"""
class Array(list):
    def __init__(self, capacity: int):
        # super().__init__()
        self.capacity = capacity

    def append(self, value):
        if len(self) < self.capacity:
            super().append(value)


arr = Array(2)
arr.append("d")
arr.append(6)
print(arr)
