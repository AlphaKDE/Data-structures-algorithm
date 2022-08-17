"""a stack is a Last-in First-Out datat structure AKA LIFO, to implement a stack in python we must 
look at the push and pop methods, it is like a stack of books, to add a book you "push" the book and to remove a book 
you must "pop" it off the stack, all the push and pop operations are to the top of the stack """

# implimenting stacks using list in python

from ast import List


my_stack = list()
my_stack.append("item 1")  # the first item to but placed in the stack
my_stack.append("item 2")  # second item
my_stack.append("item 3")  # third item
my_stack.append("item 4")  # forth item

print(my_stack)  # will output ['item 1', 'item 2', 'item 3', 'item 4']

print(my_stack.pop())  # removes item 4
print(my_stack.pop())  # removes item 3
print(my_stack)

# We can write a wrapper class for additional functionality than just append and pop


class Stack():
    """a class to implement a stack in python"""

    def __init__(self):  # first we must create a constructor
        self.stack = list()  # that contructor is really a list in python with all of its methods

    def push(self, item):  # we are defining the push method of the
        self.stack.append(item)  # using the list append method

    def pop(self):
        if len(self.stack) > 0:  # checks to see if the stack object is empty
            # using the pop method in python to remove the last item in the stack
            return self.stack.pop()
        else:
            return None

    def peek(self):  # defining the peek method for a stack
        if len(self.stack) > 0:  # checks to see if the stack is emptu
            # returns the first element at the top of the stack, but it is the last element of a list using bracket notation
            return self.stack[len(self.stack) - 1]
        else:
            return None

    def __str__(self):
        # showing the string representation of the list if someone wants to see the whole stack
        return str(self.stack)

# Stack using the wrapper class


my_stack1 = Stack()
my_stack1.push("item 1")  # pushes item 1 to the stack
my_stack1.push("item 2")  # pushes item 2 to the stack
print(my_stack1.pop())
print(my_stack1.peek())
print(my_stack1)
