import os
class Node:
    """A simple implementation of a node in a linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """A simple implementation of a singly linked list."""
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """Prints the values of the nodes in the linked list."""
        if self.length == 0:
            return None
        elif self.length == 1:
            print(self.head.value)
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def append(self, value):
        """Adds a new node with the given value to the end of the linked list."""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def delete_last_node(self):
        """Deletes the last node in the linked list."""
        if self.length == 0:
            return None
        elif self.length == 1:
            deleted_node = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return deleted_node
        else:
            current_node = self.head
            while current_node:
                if current_node.next == self.tail:
                    deleted_node = self.tail
                    current_node.next = None
                    self.tail = current_node
                    break
                current_node = current_node.next
            self.length -= 1
            return deleted_node
        
        

# Clear console
os.system("clear")
my_linked_list = LinkedList(4)
print(my_linked_list.head.value)  # Output: 4
my_linked_list.append(5)
print(my_linked_list.tail.value)  # Output: 5
print(my_linked_list.delete_last_node().value)  # Output: 5