class Array(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = list()

    def append(self, data):
        if len(self.array) < self.capacity:
            self.array.append(data)
        else:
            return self._overflow()

    def pop(self):
        return self.array.pop()

    def is_empty(self) -> bool:
        if not len(self.array):
            return True
        return False


    def _overflow(self):
        print("you reached the limit!")

if __name__ == "__main__":
    l = Array(1)
    l.append(1)
    l.append(4)
    print(l.is_empty())