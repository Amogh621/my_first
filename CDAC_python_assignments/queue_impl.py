from class_queue import Queue

q=Queue()

q.enqueue('amogh')
q.enqueue(10)
q.enqueue(4.5)
print(q.front())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.qlog.close()
