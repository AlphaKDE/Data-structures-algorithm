"""A linked list is a collection of nodes, where one node points to another, 
the first node is called head or root node  and it is used as the starting point for any iteration through the list 
to determine the end of the list, the last node must point to none"""

# Operations

# find(data)
# add(data)
# remove(data)
# print_list

# attributes
# root- pointer to the beginning of the list
# size- number of nodes in a list

# python implimentation

# we must firts create a node class:


class Node:

    """Node class that will be used to impliment linked lists in python"""
    # comes with 3 parameter, the data passed(d), the next node(n),the previous node(p)

    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p  # this parameter is only used for doubly linked lists

    def __str__(self):  # to return a string representation of the node
        return ('(' + str(self.data)+')')

# Linked list Class: there are 4 methods in a linked list
# add- recieves a piece of data, creates a new Node, than set its pointer to the root node

# find - iterates through nodes until it finds the data passed in, if it finds it it will return it otherwise it will return none

# remove-

# print_list-iterates the list and prints each node


class LinkedList:
    def __init__(self, r=None):  # one parameter which is the root node
        # has two attributes we keep track of the root node and the size
        self.root = r
        self.size = 0

    def add(self, d):  # the add method
        # we create an instance of the Node class
        new_node = Node(d, self.root)
        self.root = new_node  # set the root to the new_node
        self.size += 1  # increment the size since we are now adding a new node

    def find(self, d):
        this_node = self.root  # starting at the root node, which we call 'this node'
        while this_node is not None:  # iterating through the list using a while loop
            if this_node.data == d:  # a condition that checks if we find the data
                return d  # return the data if we find it
            else:
                this_node = this_node.next_node  # else we move on to the next node
            return None  # if we finish looping and we do not find the data we return None

    def remove(self, d):
        this_node = self.root
        prev_node = None
        while this_node is not None:  # using a while loop to check if it is a valid node
            if this_node.data == d:
                if prev_node is not None:  # checks to see if the data is in a non-root
                    # we are changing the previous nodes pointer to this nodes next node
                    prev_node.next_node = this_node.next_node
                else:
                    # if the node is in the root, we just changed the pointer to the second node in the list, which effectively deletes the root node
                    self.root = this_node.next_node
                self.size -= 1
                return True  # data removed
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False  # data not found

    def print_list(self):  # print operation
        this_node = self.root  # starting from the root
        while this_node is not None:  # we are iterating through the list starting from the root, while it is a valid node
            print(this_node, end='->')
            this_node = this_node.next_node  # setting the node to the next node
        print('None')  # print out nonw when we finish iterating


myLinkedList = LinkedList()
myLinkedList.add(5)
myLinkedList.add(8)
myLinkedList.add(12)
myLinkedList.print_list()

print(f"size={str(myLinkedList.size)}")
myLinkedList.remove(8)
myLinkedList.print_list()
print(f"size={str(myLinkedList.size)}")
