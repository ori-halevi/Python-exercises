class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinaryTree(object):
    def __init__(self):
        self._root = None

    def search(self, number: int | float):
        return self._search_recursive(self._root, number)

    def _search_recursive(self, root, value) -> object:
        if not root:
            return False
        elif value == root.data:
            return True
        elif root.data > value:
            return self._search_recursive(root.left, value)
        elif root.data < value:
            return self._search_recursive(root.right, value)

    def _search_location(self, value):
        return self._search_location_recursive(self._root, value, self._root)

    def _search_location_recursive(self, root, value, branch) -> object:
        if not root:
            location = None
            return location
        elif value == root.data:
            location = branch
            return location
        elif root.data > value:
            return self._search_location_recursive(root.left, value, branch.left)
        elif root.data < value:
            return self._search_location_recursive(root.right, value, branch.right)

    def insert(self, number: int | float):
        self._root = self._insert_recursive(self._root, number)

    def _insert_recursive(self, root, data) -> TreeNode:
        if root:
            if root.data is None:
                return TreeNode(data)
        if not root:
            return TreeNode(data)
        elif data > root.data:
            root.right = self._insert_recursive(root.right, data)
        elif data < root.data:
            root.left = self._insert_recursive(root.left, data)
        return root

    def delete(self, number: int | float):
        if self.search(number):
            temp_tree = self._ret_list_copy(number)
            for child in temp_tree[::-1]:
                self._search_location(child).data = None
            self._search_location(number).data = None
            for child in temp_tree:
                self.insert(child)

    def _ret_list_copy(self, value):
        self._temp_holder = list()
        value_location = self._search_location(value)
        self._copy_to_temp_list(value_location)
        return self._temp_holder

    def _copy_to_temp_list(self, value_location):
        if not value_location.right and not value_location.left:
            return
        if value_location.right:
            self._temp_holder.append(value_location.right.data)
            self._copy_to_temp_list(value_location.right)
        if value_location.left:
            self._temp_holder.append(value_location.left.data)
            self._copy_to_temp_list(value_location.left)

    def in_order(self):
        self._in_order_recursive(self._root)

    def _in_order_recursive(self, root):
        if root:
            if root.left:
                self._in_order_recursive(root.left)
            elif root.right:
                print(root.data, end=" ")
            if root.left and root.right:
                print(root.data, end=" ")
            if root.right:
                self._in_order_recursive(root.right)
            elif root.left:
                print(root.data, end=" ")
            if not root.left and not root.right:
                print(root.data, end=" ")


if __name__ == "__main__":
    def print_by_shape(root, level=0):
        if root:
            print_by_shape(root.right, level + 1)
            print(" " * 5 * level + " --{" + str(root.data))
            print_by_shape(root.left, level + 1)


    o = BinaryTree()
    o.insert(9)
    o.insert(11)
    o.insert(18)
    o.insert(3)
    o.insert(30)
    o.insert(17)
    o.insert(16)
    o.insert(16.5)
    o.insert(14)
    o.insert(15)
    o.in_order()
    # print(o._root.right.data)
    # print(o.search(3))
    print_by_shape(o._root)

    o.delete(18)
    # o.delete(14)
    o.delete(16)

    o.in_order()
    print()
    print_by_shape(o._root)
