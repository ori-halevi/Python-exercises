class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def search(self, value):
        return self._search_recursive(self.root, value)

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
        return self._search_location_recursive(self.root, value, self.root)

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

    def insert(self, data):
        self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(self, root, data) -> TreeNode:
        if root is None:
            return TreeNode(data)
        elif data > root.data:
            root.right = self._insert_recursive(root.right, data)
        elif data < root.data:
            root.left = self._insert_recursive(root.left, data)
        return root

    def _delete_recursive(self, root, value):
        if root is None:
            return None
        elif value == root.data:
            return None
        elif value > root.data:
            root.right = self._delete_recursive(root.right, value)
        elif value < root.data:
            root.left = self._delete_recursive(root.left, value)
        return root

    def delete(self, data):
        if self.search(data):
            self.root = self._delete_recursive(self.root, data)

    def ret_list_copy(self, value):
        self.temp_holder = list()
        value_location = self._search_location(value)
        self._copy_to_temp_list(value_location)
        return self.temp_holder

    def _copy_to_temp_list(self, value_location):
        if not value_location.right and not value_location.left:
            return
        if value_location.right:
            self.temp_holder.append(value_location.right.data)
            self._copy_to_temp_list(value_location.right)
        if value_location.left:
            self.temp_holder.append(value_location.left.data)
            self._copy_to_temp_list(value_location.left)

def in_order(root):
    if root:
        in_order(root.left)
        print(root.data, end=" ")
        in_order(root.right)

def print_by_shape(root, level = 0):
    if root:
        print_by_shape(root.right, level + 1)
        print(" " * 5 * level +" --{" + str(root.data))
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

print(o.search(3))
print(o.ret_list_copy(18))
o.delete(18)

in_order(o.root)
print()
print_by_shape(o.root)
