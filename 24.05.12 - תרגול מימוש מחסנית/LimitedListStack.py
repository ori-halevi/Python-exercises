import LinkedListClass


class LimitedListStack(object):

    def __init__(self, capacity):
        self.LStack = LinkedListClass.LinkedList()
        self.capacity = capacity

    def push(self, data):
        if self.LStack.get_len() < self.capacity:
            self.LStack.add_at_head(data)
        else:
            return self._overflow()

    def pop(self):
        return self.LStack.pop_at_head()

    def peek(self):
        return self.LStack.get_head()

    def is_empty(self):
        return self.LStack.is_empty()

    def _overflow(self):
        print("you reached the limit!")


if __name__ == "__main__":
    l = LimitedListStack(3)
    l.push(3)
    l.push(4)
    l.push(5)
    l.push(6)
    print(l.peek())
