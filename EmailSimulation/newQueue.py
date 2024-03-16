class Queue:
    '''
    this class represents a (First in First Out)FIFO data structure, also called a queue
    '''
    def __init__(self):
        '''
        constructor method for the queue
        '''
        self.queue = []

    def put(self, element):
        '''
        inserts a new element into the queue

        parameters:
            element: item to be inserted
        '''
        self.queue.insert(0, element)

    def get(self):
        '''
        retrieves the next element
        '''
        return self.queue.pop(self.size() - 1)

    def clear(self):
        '''
        clears the queue
        '''
        self.queue.clear()

    def size(self):
        '''
        returns: size of queue
        '''
        return len(self.queue)