
class Node:

    def __init__(self, value):

        self.data = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None


    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node


    def delete_tail(self):
        if (self.head == None):
            return None
        
        current_tail = self.tail
        if self.head.next == None:
            self.head = None
            self.tail = None
        else: 
            self.tail = current_tail.prev
            self.tail.next = None
            current_tail.prev = None
        



    def prepend(self, value):

        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node


    def delete_head(self):
        old_head = self.head
        if self.head == None:
            return None
        elif self.head.next == None:
            self.head = None
            self.tail = None
        else: 
            self.head = old_head.next
            self.head.prev = None
            old_head.next = None



    def search(self, value):
        curr = self.head

        while curr:
            if curr.data == value:
                return f'Found: {curr.data}'
            curr = curr.next

        return None


    def __str__(self):
        print_head = self.head
        output_string = ''

        while(print_head):
            output_string += f' -> {print_head.data}'
            print_head = print_head.next

        return output_string

# Instantiate SinglyLinkedList object
linked_list = DoublyLinkedList()

print("Linked List")
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.prepend(1)
# ->  1 -> 2 -> 3 -> 4
print(linked_list)

linked_list.delete_tail()



print("After delete ")
# ->  2 -> 3
print(linked_list)


print('Search')
print(linked_list.search(3))
# Found: 3
