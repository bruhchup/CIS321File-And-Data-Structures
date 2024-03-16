import os
from client import Client
from message import Message
from server import Server
from time import sleep 

def main():
    '''
    Simulates the starting of a server and the exchange of emails between two people
    '''
    server = Server()
    Bob = Client('Bob', 3, server)
    Sue = Client('Sue', 5, server)

    #counters for Bob and Sues messages
    bobCounter = 0
    sueCounter = 0
    #Variable to hold the time elapse since the loop started
    timeElapsed = 0

    while bobCounter + sueCounter <= 20:
        if timeElapsed % Bob.waitTime == 0 and bobCounter <= 10:
            bobCounter += 1
            Bob.send(Message(Bob.name, Sue.name, f'Hello Sue, This is my {bobCounter} attempt at reaching you\n'))
        if timeElapsed % Sue.waitTime == 0 and sueCounter <= 10:
            if bobCounter >= 10:
                Sue.send(Message(Sue.name, Bob.name, f'Did you actually need anything!? You are wasting my time!!!\n'))    
            elif bobCounter >= 2:
                Sue.send(Message(Sue.name, Bob.name, f'Hello Bob, I see your message. Please check your inbox because I am replying to every email you send me. Stop flooding my inbox.\n'))   
            else:
                Sue.send(Message(Sue.name, Bob.name, f'Hello Bob, I see your email. What is it that you need?\n'))
            sueCounter += 1
        server.write(timeElapsed)
        #Program sleeps for one second after executing the loop; timeElapsed is incremented to account for the time slept.
        sleep(1)
        timeElapsed += 1

if __name__ == '__main__':
    main()