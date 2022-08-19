class BinaryTree:

    def __init__(self, value):

        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):

        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = BinaryTree(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = BinaryTree(value)
                else:
                    self.right.insert(value)
        else:
            self.value = value

    def search(self, value):
        if value < self.value:
            if self.left is None:
                return f'{value} not found'
            return self.left.search(value)
        elif value > self.value:
            if self.right is None:
                return f'{value} not found'
            return self.right.search(value)
        else:
            return f'{self.value} found!'
    

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print( self.value),
        if self.right:
            self.right.print_tree()

bt = BinaryTree(10)
bt.insert(15)
bt.insert(20)
bt.insert(5)
bt.insert(0)
bt.insert(52)

bt.print_tree()

print(bt.search(47))
print(bt.search(0))