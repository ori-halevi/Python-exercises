class Node(object):
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
    def push(self, new_node: Node) -> None:
        new_node.next = self.head
        self.head = new_node

