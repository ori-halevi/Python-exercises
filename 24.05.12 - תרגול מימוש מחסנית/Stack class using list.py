class Stack(object):
    def __init__(self):
        self.stack = list()

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()

    def is_empty(self) -> bool:
        return not not self.stack

    def peek(self):
        x = self.stack.pop()
        self.stack.append(x)
        return x

    def __str__(self):
        return str(self.stack)


if __name__ == "__main__":

    st1 = Stack()
    print(type(st1))
    st1.push(9)
    print(st1)
    st1.pop()
    print(st1)
    print(st1.is_empty())
    st1.push(5)
    print(st1)
    print(st1.peek())
    print(st1.is_empty())


    m = Stack()
    m.push("d")
    m.push("u")
    print(m)