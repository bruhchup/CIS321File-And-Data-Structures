import os
from time import sleep
from time import time
from newQueue import Queue
from datetime import datetime

class Server:

    #Creates log to record communication transactions
    LOG = open('log.csv','a')

    def __init__(self):
        '''
        Initializes the server and its associated data structure (queue)
        Records the time the server was created
        '''
        self.time = int(time())
        self.queue = Queue()

    def write(self, timeElapsed):
        '''
        writes message details to the csv log file
        params:
            timeElapsed: A time keeping object; purposed to be used with seconds
        '''
        while self.queue.size() > 0:
            #If the measurement of time is divisible by 4, the server will get every element in the queue
            if timeElapsed % 4 == 0:
                while self.queue.size() > 0:
                    msgDetails = self.queue.get()
                    print(f'{msgDetails}\n')
                    self.LOG.write(f'{msgDetails.sender},{msgDetails.recipient},{datetime.now()}\n')
            else:
                break
            self.LOG.flush()
            