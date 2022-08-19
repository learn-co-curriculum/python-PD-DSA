# Implement a stack


class Stack:
    def __init__(self, limit = None):
        self.stack = []
        self.limit = limit

    def push(self, value):
        if self.full():
            print('Stack Overflow')
            return

        self.stack.append(value)
        print(f'Push {value}: {self.stack}')


    def pop(self):
        if self.stack:
            print(f'Pop: {self.stack.pop()}')

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def empty(self):
        return len(self.stack) == 0

    def full(self):
        return self.limit == len(self.stack)

    def search(self, target):
        for i in range(len(self.stack)):
            if self.stack[i] == target:
                print(f'Found: { len(self.stack) - i}')



stk = Stack()
stk.push(1)
stk.push(3)
stk.push(2)
stk.push(4)
stk.push(7)

print(stk.peek())
print(stk.search(4))

stk.pop()
stk.pop()
stk.pop()
stk.pop()
stk.pop()
print(stk.empty())
print(stk.size())
