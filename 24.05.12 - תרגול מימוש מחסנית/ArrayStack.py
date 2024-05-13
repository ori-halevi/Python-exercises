import Array
class ArrayStack(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.array_stack = Array.Array(self.capacity)

    def push(self, data):
        self.array_stack.append(data)

    def pop(self):
        return self.array_stack.pop()

    def peek(self):
        f = self.array_stack.pop()
        self.array_stack.append(f)
        return f

    def is_empty(self):
        return self.array_stack.is_empty()


if __name__ == "__main__":
    l = ArrayStack(2)
    l.push(7)
    l.push(7)
    l.push(7)
    l.push(6)
    print(l.peek())
