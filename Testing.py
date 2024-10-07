#Linked List - Without Node
class LinkedList:
    #Constructor
    def __init__(self):
        self.front = None
        self.back = None

#Linked List with Node
class LinkedList:
    class Node:
        def __init__(self, data, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev