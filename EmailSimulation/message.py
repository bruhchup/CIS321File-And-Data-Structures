from datetime import datetime

class Message:

    def __init__(self, sender, recipient, text):
        '''
        Represents an email message
        
        params:
            sender: author of the email (str)
            recipient: recipient of the email (str)
            text: content of the email (str)
        '''
        self.sender = sender
        self.recipient = recipient
        self.text = text

    def __str__(self):
        '''
        formats the message to be printed in the terminal
        '''
        lineBreak = '**************************************************\n'
        return f'{lineBreak}{'|Author:':<14} {self.sender}\n{'|Recipient:':<14} {self.recipient}\n|Processed at: {datetime.now()}\n|{self.text}{lineBreak}'