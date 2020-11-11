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

    # traverse a linked list
    def traverseSLL(self):
        if self.head is None:  # O(1)
            print("This linked list does not exist")
        else:
            node = self.head  # O(1)
            while node is not None:  # O(n)
                print(node.value)
                node = node.next

    # search for node in linked list
    def searchSLL(self, nodeValue):
        if self.head is None:
            print("This linked list does not exist")  # O(1)
        else:
            node = self.head  # O(1)
            while node is not None:  # O(n)
                if node.value == nodeValue:  # O(1)
                    return node.value
                node = node.next
            return "Value doesn't exist in this list."

    # delete node from linked list
    def deleteNode(self, location):
        if self.head is None:  # O(1)
            print('This linked list does not exist')
        else:
            # beginning of linked list
            if location == 0:
                if self.head == self.tail:  # O(1)
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            # last node of the linked list
            elif location == 1:
                if self.head == self.tail:  # O(1)
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:  # O(n)
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            # delete node from middle of linked list
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:  # O(n)
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

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

# traverse the LL
singlyLinkedList.traverseSLL()

# search LL
print(singlyLinkedList.searchSLL(5))
print(singlyLinkedList.searchSLL(55))

# delete node
singlyLinkedList.deleteNode(3)  # deletes 7
print([node.value for node in singlyLinkedList])

''' creation of singly linked list
# node1= Node(1)
# node2= Node(2)

# singlyLinkedList.head = node1
# singlyLinkedList.head.next = node2 #O(n)
# singlyLinkedList.tail = node2
'''
