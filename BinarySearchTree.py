class BinarySearchTree:

    def __init__(self, value):

        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):

        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def search(self, target):

        if target < self.value:
            if self.left is None:
                return f'{target} not found'
            return self.left.search(target)

        elif target > self.value:
            if self.right is None:
                return f'{target} not found'
            return self.right.search(target)

        else:
            return f'{self.value} found!'


    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print( self.value),
        if self.right:
            self.right.print_tree()


bt = BinarySearchTree(10)
bt.insert(35)
bt.insert(6)
bt.insert(4)
bt.insert(8)
bt.insert(25)
bt.insert(40)
print('Right')
print(bt.right.value)
print('left')
print(bt.left.value)


# bt.print_tree()

print(bt.search(47))
print(bt.search(8))

