from LL import *

class ConfigList(LinkedList):

    def __init__(self, config:bool):
        '''
        Constructor class that determines whether the Linked List is a queue or stack

        params:
            config: a boolean value to determine state:
                True: Queue
                False: Stack
        '''
        super().__init__()
        self.config = config

    def insert(self, cargo):
        '''
        inserts a new node into the linked list
        
        params:
            cargo: data to be inserted
        '''
        if self.config is True:
            self.insertToBack(cargo)
        else:
            self.insertToBack(cargo)

    def pop(self):
        '''
        pops a node from the linked list
        '''
        if self.config is True:
            return self.popFromFront()
        else:
            return self.popFromBack()

    def __str__(self):
        '''
        returns a string indicating the type of data structure and the number of nodes
        '''
        if self.config is True:
            return f'queue object with size {self.size()}'
        else:
            return f'stack object with size {self.size()}'