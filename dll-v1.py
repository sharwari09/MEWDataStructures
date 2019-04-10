class Node(object):

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
	
    

class DoublyLinkedList(object):
    
    def __init__(self, val):
	node = Node(val)
        self.front = node
	self.rear = node
	print("Front: {} | Rear: {}".format(self.front.val, self.rear.val))


    def insertNodeAtRear(self, val):
	new_node = Node(val)
	print("New node with value: {} is created".format(val))
	self.rear.next = new_node
	new_node.prev = self.rear
	self.rear = new_node
	print("Front: {} | Rear: {}".format(self.front.val, self.rear.val))

    
    def insertNodeAtFront(self, val):
        new_node = Node(val)
        print("New node with value: {} is created".format(val))
        self.front.prev = new_node
        new_node.next = self.front
        self.front = new_node
        print("Front: {} | Rear: {}".format(self.front.val, self.rear.val))    


    def delNodeFromFront(self):
        temp = self.front
        self.front = self.front.next
        if self.front is None:
	    self.rear = None
        else:
            self.front.prev = None

    def delNodeFromRear(self):
        temp = self.rear
        self.rear = self.rear.prev
        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None

    def getNodeWithVal(self, val):
	temp = self.front
        while temp.next is not None:
            if temp.val == val:
		return temp
	    temp = temp.next
	return None


    def printList(self):
	temp = self.front
	dll = []
	while temp.next is not None:
	    dll.append(temp.val)
	    temp = temp.next
        print(dll)

   


dll = DoublyLinkedList(3)
dll.insertNodeAtRear(4)
dll.insertNodeAtRear(5)
dll.insertNodeAtRear(6)
dll.insertNodeAtRear(7)
dll.printList()
dll.insertNodeAtFront(10)
dll.insertNodeAtFront(11)
dll.insertNodeAtFront(12)
dll.insertNodeAtFront(13)
dll.printList()
dll.delNodeFromFront()
dll.delNodeFromFront()
dll.printList()
dll.delNodeFromRear()
dll.delNodeFromRear()
dll.delNodeFromFront()
dll.delNodeFromRear()
dll.printList()
dll.delNodeFromFront()
dll.delNodeFromRear()
dll.printList()

