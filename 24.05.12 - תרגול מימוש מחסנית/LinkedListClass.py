class Node(object):
    def __init__(self, data: str | int):
        self.data = data
        self.next = None


class LinkedList(object):
    head = None

    def add(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def add_at_head(self, data):
        new_node_holder = Node(data)
        new_node_holder.next = self.head
        self.head = new_node_holder


    def get_head(self):
        if self.head:
            return self.head.data
        else:
            return None

    def pop_at_head(self):
        data_to_del = self.head.data
        self.head = self.head.next
        return data_to_del

    def pop_at_tail(self):
        if not self.get_len():
            return
        current = self.head
        if self.get_len() >= 2:
            for i in range(self.get_len() - 2):
                current = current.next
            data_to_pop = current.next.data
            current.next = None
            return data_to_pop
        elif self.get_len() == 1:
            data_to_pop = current.data
            current.next = None
            return data_to_pop

    def is_empty(self) -> bool:
        return self.head is None

    def get_len(self):
        count = 0
        if not self.is_empty():
            current = self.head
            while current:
                count += 1
                current = current.next
        return count

    def print_ll(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def get_ll(self):
        current = self.head
        if current:
            my_tuple = current.data
            current = current.next
            while current:
                my_tuple = str(my_tuple) + ", " + str(current.data)
                current = current.next
            return my_tuple

    def get_ll_in_list(self):
        current = self.head
        temp_list = list()
        if not current:
            return
        while current:
            temp_list.append(current.data)
            current = current.next
        return temp_list

    def average(self):
        if not self.head:
            return 0
        count = 0
        sum = 0
        node = self.head
        while node:
            sum += node.data
            node = node.next
            count += 1
        return sum

if __name__ == "__main__":
    ob = LinkedList()
    print(ob.print_ll())
    print(ob.is_empty())
    ob.add(8)
    ob.add(9)
    ob.add(10)
    ob.add(11)
    ob.add(12)
    ob.add_at_head(7)
    ob.print_ll()
    print("is empty:", ob.is_empty())
    print("all", ob.get_ll())
    print(ob.get_len())
    print("del head:", ob.pop_at_head())
    print("all:", ob.get_ll())
    print("pop tail:", ob.pop_at_tail())
    print("all:", ob.get_ll())
    print(ob.average())