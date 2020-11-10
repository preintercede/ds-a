class Node: 
    def __init__(self, value=None):
        self.value = value
        self.next = None #O(n)

class SinglyLinkedList:
    def __init__(self):
        self.head = None #O(n)
        self.tail = None #O(n)


# Time complexity of creating a singly linked list is O(1)
# Soace complexity also O(1)

singlyLinkedList = SinglyLinkedList()
node1= Node(1)
node2= Node(2)

singlyLinkedList.head = node1
singlyLinkedList.head.next = node2 #O(n)
singlyLinkedList.tail = node2