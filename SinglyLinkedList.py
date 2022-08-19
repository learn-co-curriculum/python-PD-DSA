
class Node:

    def __init__(self, value):

        self.data = value
        self.next = None


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def append(self, value):

        pass

    def delete_tail(self):
        pass

    def prepend(self, value):

        pass

    def delete_head(self):
        pass

    def search(self, value):
        pass

    def __str__(self):
        print_head = self.head
        output_string = ''

        while(print_head):
            output_string += f' -> {print_head.data}'
            print_head = print_head.next

        return output_string

# Instantiate SinglyLinkedList object
# linked_list = SinglyLinkedList()

# print("Linked List")
# linked_list.append(2)
# linked_list.append(3)
# linked_list.append(4)
# linked_list.prepend(1)
# ->  1 -> 2 -> 3 -> 4
# print(linked_list)

# linked_list.delete_tail()
# linked_list.delete_head()
# print("After delete ")
# ->  2 -> 3
# print(linked_list)

# print('Search')
# print(linked_list.search(3))
# Found: 3
