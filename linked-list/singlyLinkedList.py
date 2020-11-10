class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None  # O(n)


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # O(n)
        self.tail = None  # O(n)

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # insert in Linked List
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:  # O(1)
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:  # O(1)
                # beginning of the list
                newNode.next = self.head
                self.head = newNode
            elif location == 1:  # O(1)
                # add to end of the list
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                # add to middle of linked list
                tempNode = self.head
                index = 0
                while index < location - 1:  # O(n)
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next  # O(1)
                tempNode.next = newNode
                newNode.next = nextNode


# Time complexity of creating a singly linked list is O(1)
# Space complexity also O(1)

singlyLinkedList = SinglyLinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)


# add to beginning of LL
singlyLinkedList.insertSLL(5, 0)

# add to middle of LL
singlyLinkedList.insertSLL(7, 3)

# add to end of LL
singlyLinkedList.insertSLL(10, 1)


print([node.value for node in singlyLinkedList])

''' creation of singly linked list
# node1= Node(1)
# node2= Node(2)

# singlyLinkedList.head = node1
# singlyLinkedList.head.next = node2 #O(n)
# singlyLinkedList.tail = node2
'''
