class Node:

    def __init__(self, cargo, nextNode):
        '''
        Constructor method; initializes a node
        
        params:
            cargo: data to be inserted into the node
            nextNode: points to the next node in the linked list
        '''
        self.cargo = cargo
        self.nextNode = nextNode

    def setNext(self, nextNode):
        self.nextNode = nextNode

    def getCargo(self):
        return self.cargo

    def __str__(self):
        return str(self.cargo)

class LinkedList:
    def __init__(self):
        '''
        Constructor method; initializes an empty linked list object
        '''
        self.head = None

    def insertToFront(self, cargo):
        '''
        inserts a Node to the front of the linked list

        params:
            cargo: data to be inserted
        '''
        if self.head is None:
            self.head = Node(cargo, None)
        else:
            node = Node(cargo, self.head)
            self.head = node

    def insertToBack(self, cargo):
        '''
        inserts a node to the back of the linked list
        
        params:
            cargo: data to be inserted
        '''
        node = self.head
        newNode = Node(cargo, None)
        if node is not None and node.nextNode is not None:
            while node.nextNode is not None:
                node = node.nextNode
            node.nextNode = newNode
        elif node is not None:
            node.nextNode = newNode
        elif node is None:
            self.head = newNode
        else:
            newNode = Node(cargo, None)
            self.head = newNode

    def popFromFront(self):
        '''
        pops a node from the front of the linked list
        '''
        if self.head is not None:
            placeholder = self.head
            self.head = self.head.nextNode
            return placeholder.cargo 

    def popFromBack(self):
        '''
        pops a node from the back of the linked list
        '''
        if self.head is not None and self.head.nextNode is not None:
            currNode = self.head
            prevNode = self.head
            while currNode.nextNode is not None:
                currNode = currNode.nextNode
                if prevNode.nextNode is not currNode:
                    prevNode = prevNode.nextNode
            prevNode.nextNode = None
            return currNode.cargo
        elif self.head is None:
            return None
        else:
            currNode = self.head
            self.head = None
            return currNode.cargo

    def size(self):
        '''
        returns the size of the list
        '''
        if self.head is not None:
            node = self.head
            count = 1
            while node.nextNode is not None:
                node = node.nextNode
                count += 1
        else:
            return 0
        return count

    def empty(self):
        '''
        empties the linked list
        '''
        self.head = None

    def __str__(self):
        s = 'Linked List\n'
        node = self.head
        while node is not None:
            if node.nextNode is not None:
                s += f'{str(node)} -> '
            else:
                s += str(node)
            node = node.nextNode
        return s