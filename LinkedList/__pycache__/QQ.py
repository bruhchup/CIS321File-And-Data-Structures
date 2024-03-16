import os
from LL import *

class Queue:
    
    def __init__(self):
        self.queue = LinkedList()
        
    def push(self, cargo):
        '''
        pushes elements into queue
        
        params:
            cargo: data to be inserted
        '''
        self.queue.insertToBack(cargo)
        
    def pop(self):
        '''
        pops elements from the queue
        '''
        return self.queue.popFromFront()
    
    def empty(self):
        '''
        empties the queue
        '''
        self.queue.empty() 