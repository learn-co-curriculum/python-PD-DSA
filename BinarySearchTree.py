class BinarySearchTree:

    def __init__(self, value):

        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        pass

    def search(self, target):
        pass

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print( self.value),
        if self.right:
            self.right.print_tree()


# bt = BinarySearchTree(10)
# bt.insert(35)
# bt.insert(6)
# bt.insert(4)
# bt.insert(8)
# bt.insert(25)
# bt.insert(40)
# print('Right')
# print(bt.right.value)
# print('left')
# print(bt.left.value)


# bt.print_tree()

# print(bt.search(47))
# print(bt.search(8))

