class Client:
    
    def __init__(self, name, waitTime, server):
        '''
        Handles the name of a client, they're delay in sending automated messages, 
        and the server they are sending to
        
        params:
            name: client name
            waitTime: message delay
            server: server to connect to
        '''
        self.name = f'{name}@hmail.com'
        self.waitTime = waitTime
        self.server = server
        
    def send(self, message):
        '''
        inserts the message into the servers queue
        
        params:
            message: Message object
        '''
        self.server.queue.put(message)
        
        
        
        