import LinkedListClass

class Stack(object):
    def __init__(self):
        self.stack = LinkedListClass.LinkedList()

    def push(self, value):
        self.stack.add_at_head(value)

    def pop(self):
        return self.stack.pop_at_head()

    def peek(self):
        return self.stack.get_head()

    def is_empty(self):
        return self.stack.is_empty()

    def get_len(self):
        return self.stack.get_len()

    def flip(self):
        temp_ll = LinkedListClass.LinkedList()
        replica_stack = LinkedListClass.LinkedList()
        for i in self.stack.get_ll_in_list():
            replica_stack.add(i)
        if replica_stack.is_empty():
            return
        else:
            while self.stack.get_len() > temp_ll.get_len():
                temp_ll.add(replica_stack.pop_at_tail())
            return temp_ll.get_ll()

    def __str__(self):
        return str(self.stack.get_ll())


if __name__ == "__main__":
    ob = Stack()
    ob.push(4)
    print(ob)
    ob.pop()
    print(ob)
    ob.peek()
    print(ob)
    ob.push(3)
    print(ob)
    ob.push(4)
    print(ob)
    ob.push(5)
    print(ob)
    print(ob.pop())
    print(ob)
    # print(ob.is_empty())
    #
    # ob.push(6)
    # print(ob)
    # ob.push(7)
    # print(ob)
    # ob.push(8)
    # print(ob)
    # ob.push(9)
    # print(ob)
    # ob.push(10)
    # print(ob)
    # print("...")
    # print(ob.flip())