class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def search(self, value):
        return self.search_rec(self.root, value)

    def search_rec(self, root, value) -> object:
        if not root:
            return False
        elif value == root.data:
            return True
        elif root.data > value:
            return self.search_rec(root.left, value)
        elif root.data < value:
            return self.search_rec(root.right, value)

    def search_location(self, value):
        return self.search_location_rec(self.root, value, self.root)

    def search_location_rec(self, root, value, branch) -> object:
        # location = "root"
        if not root:
            location = "Not Found"
            return location
        elif value == root.data:
            location = branch.data
            return location
        elif root.data > value:
            # location = location + ".left"
            return self.search_location_rec(root.left, value, branch.left)
        elif root.data < value:
            # location = location + ".right"
            return self.search_location_rec(root.right, value, branch.right)

    def insert(self, data):
        self.root = self.insert_rec(self.root, data)

    def insert_rec(self, root, data) -> TreeNode:
        if root is None:
            return TreeNode(data)
        elif data > root.data:
            root.right = self.insert_rec(root.right, data)
        elif data < root.data:
            root.left = self.insert_rec(root.left, data)
        return root

    def delete(self, data):
        pass

    def ret_list_copy(self, value):
        self.temp_holder = list()
        value_location = self.search_location(value)
        return self.copy_to_temp_list(value_location)


    # def copy_to_temp_list(self, branch, value_location):
    def copy_to_temp_list(self, value_location):
        if not value_location.right:
            self.temp_holder.append(value_location)
            return
        if not value_location.left:
            self.temp_holder.append(value_location)
            return
        self.temp_holder.append(value_location.right)
        self.copy_to_temp_list(value_location.right)
        self.temp_holder.append(value_location.left)
        self.copy_to_temp_list(value_location.left)
        # self.delete_rec(self.root, data)

    # def delete_rec(self, root: TreeNode, data):
    #     if not root:
    #         return
    #     elif data == root.data:




    def in_order(self):
        pass

o = BinaryTree()
o.insert(9)
o.insert(11)
o.insert(18)
o.insert(3)
o.insert(30)
o.insert(17)
# print(o.root.right.data)
print()
print(o.search(3))
print(o.search_location(17))
# print(o.ret_list_copy(11))