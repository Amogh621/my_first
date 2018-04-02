import time

class Queue:
    
    def __init__(self):
        self.new_queue = []
        self.qlog = open("queue_log.txt", "w+")
        now = time.asctime( time.localtime(time.time()) )
        self.qlog.write(now + ":" + "New queue created.\n")
        
    def enqueue(self, item):
        self.new_queue.append(item)
        now = time.asctime( time.localtime(time.time()) )
        self.qlog.write(now + ":" + "New element enqueued.\n")

    def dequeue(self):
        now = time.asctime( time.localtime(time.time()) )
        self.qlog.write(now + ":" + "Element dequeued.\n")
        return self.new_queue.pop(0)

    def front(self):
        return self.new_queue[0]







    
