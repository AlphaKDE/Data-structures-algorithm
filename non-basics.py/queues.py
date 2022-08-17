"""Queues in python is a First-in First-Out data structures AKA FIFO, ques have two important functions
Enqueue which is when you add an item to the end of the line, and Dequeue when you remove an item 
from the front of the line"""

# implimening a queue in python
# python already offers us a deque class from the collections module
from collections import deque
from queue import Queue  # importing pythong Queue class from the queue modules

# deque is a double ended queue which allows us to add or remove items from move edd of the queue,
# for our implimentation we only need to add items at one end and pop them off at the other

my_queue = deque()  # create a deque object
my_queue.append("person 1")
my_queue.append("person 2")
print(my_queue)
print(my_queue.popleft())


"""Implementation using queue.Queue

Queue is built-in module of Python which is used to implement a queue. queue.Queue(maxsize) initializes a variable to a maximum size of maxsize. A maxsize of zero ‘0’ means a infinite queue. This Queue follows FIFO rule. 
There are various functions available in this module: 
 

maxsize _  Number of items allowed in the queue.
empty()-   Return True if the queue is empty, False otherwise.
full()- Return True if there are maxsize items in the queue. If the queue was initialized with maxsize=0 (the default), then full() never returns True.
get()-  Remove and return an item from the queue. If queue is empty, wait until an item is available.
get_nowait()- Return an item if one is immediately available, else raise QueueEmpty.
put(item)- Put an item into the queue. If the queue is full, wait until a free slot is available before adding the item.
put_nowait(item) - Put an item into the queue without blocking. If no free slot is immediately available, raise QueueFull.
qsize() - Return the number of items in the queue."""

# Initializing a queue
q = Queue(maxsize=3)

# qsize() give the maxsize
# of the Queue
print(q.qsize())

# Adding of element to queue
q.put('a')
q.put('b')
q.put('c')

# Return Boolean for Full
# Queue
print("\nFull: ", q.full())

# Removing element from queue
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())

# Return Boolean for Empty
# Queue
print("\nEmpty: ", q.empty())

q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())

# This would result into Infinite
# Loop as the Queue is empty.
# print(q.get())


# a wrapper class for the queue class
class Queue1:
    def __init__(self):
        self.queue = deque()  # using the deque class as a base structure

    def Enqueue(self, item):  # defining the enqueue operation
        self.queue.append(item)  # using the append method of a deque object

    def Dequeue(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        else:
            return None

    def front(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            return None

    def rear(self):
        if len(self.queue) > 0:
            return self.queue[len(self.queue) - 1]

    def getzie(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)


q = Queue1()

q.Enqueue("person 1")
q.Enqueue("person 2")
q.Enqueue("person 3")

print(q)
q.Dequeue()
print(q)
print(q.getzie())
