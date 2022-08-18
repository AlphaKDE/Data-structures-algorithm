"""A circular linked list is similar to a regular liked list except the final nodes pointer is 
the root node, instead of none, the add operation than becomes different"""

# any node we want to add will be added as the second node,
# we are going to insert the node as the second node, the root node will now be pointing to the newly added node
# the newly added node will not be pointed to the next node which was the second node.


class Node:

    """Node class that will be used to impliment linked lists in python"""
    # comes with 3 parameter, the data passed(d), the next node(n),the previous node(p)

    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p  # this parameter is only used for doubly linked lists

    def __str__(self):  # to return a string representation of the node
        return ('(' + str(self.data)+')')


class CircularLinkedlist:
    def __init__(self, r=None):  # one parameter which is the root node
        # has two attributes we keep track of the root node and the size
        self.root = r
        self.size = 0

    def add(self, d):  # add method
        if self.size == 0:  # check to see if the list is empty
            self.root = Node(d)
            # we make its next node point to itself since it is a circular list
            self.root.next_node = self.root
        else:  # if their is already atleast one node in the list
            # create a new node and insert it into the number 2 position right after the root
            new_node = Node(d, self.root.next_node)
            # than we change the roots next node to point to the new node
            self.root.next_node = new_node
        self.size += 1  # incrementing

    def find(self, d):
        this_node = self.root  # starting at the root node, which we call 'this node'
        while True:  # iterating through the list using a while loop
            if this_node.data == d:  # a condition that checks if we find the data
                return d  # return the data if we find it
            elif this_node.next_node == self.root:  # we have to do a check to see if we circled bck to the root node
                return False  # if so we must return false
            this_node = this_node.next_node  # else we move on to the next node

    def remove(self, d):
        this_node = self.root
        prev_node = None
        while True:  # using a while loop to check if it is a valid node
            if this_node.data == d:
                if prev_node is not None:  # checks to see if the data is in a non-root
                    # we are changing the previous nodes pointer to this nodes next node
                    prev_node.next_node = this_node.next_node
                else:  # if we need to delete the root
                    while this_node.next_node != self.root:  # using this while loop to find the very last node in the list
                        # updating the last node to point to the new root, since the root have changed
                        this_node = this_node.next_node
                    # updating the last node next pointer to the root
                    this_node.next_node = self.root.next_node
                    self.root = self.root.next_node  # updating the root pointer
                self.size -= 1
                return True  # data removed

            elif this_node.next_node == self.root:
                return False  # data not found
            prev_node = this_node
            this_node = this_node.next_node

    def print_list(self):  # print operation
        if self.root is None:
            return
        this_node = self.root
        print(this_node, end='->')

        # we are iterating through the list starting from the root, while it is a valid node
        while this_node.next_node != self.root:  # checks if we made it back to the loop,
            this_node = this_node.next_node  # if not we continue to iterate
            print(this_node, end='->')
        print()


# test code:
myCLL = CircularLinkedlist()
x = [5, 6, 7, 8, 9]
for i in x:
    myCLL.add(i)  # addingg items to the list
print(f"size {str(myCLL.size)}")

print(myCLL.find(8))
print(myCLL.find(12))

my_node = myCLL.root
print(my_node, end='->')

for i in range(8):  # we want to see if the last node will point to the root
    my_node = my_node.next_node
    print(my_node, end='->')
print()

myCLL.print_list()
myCLL.remove(8)
print(myCLL.remove(15))
print(f"size = {str(myCLL.size)}")
myCLL.remove(5)  # removing root node
myCLL.print_list()
