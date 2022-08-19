
class Node:

    def __init__(self, value):

        self.data = value
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def append(self, value):

        if self.head == None:
            self.head = Node(value)
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        last_node.next = Node(value)

    def delete_tail(self):
        if not self.head:
            return None

        if not self.head.next:
            self.head = None
            return
        curr = self.head
        prev = None
        while curr.next:
            prev = curr
            curr = curr.next

        prev.next = None


    def prepend(self, value):

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


    def delete_head(self):
        if self.head:
            self.head = self.head.next


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
linked_list = SinglyLinkedList()

print("Linked List")
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.prepend(1)
# ->  1 -> 2 -> 3 -> 4
print(linked_list)

linked_list.delete_tail()
linked_list.delete_head()
print("After delete ")
# ->  2 -> 3
print(linked_list)

print('Search')
print(linked_list.search(3))
# Found: 3
