class Node:

    """Node class that will be used to impliment linked lists in python"""
    # comes with 3 parameter, the data passed(d), the next node(n),the previous node(p)

    def __init__(self, d, n=None, p=None):
        self.data = d
        self.next_node = n
        self.prev_node = p  # this parameter is only used for doubly linked lists

    def __str__(self):  # to return a string representation of the node
        return ('(' + str(self.data)+')')


class DoublyLinkedlist:
    def __init__(self, r=None):
        self.root = r
        self.last = r  # extra list attribute so that we can always acess the last item
        self.size = 0

    def add(self, d):
        if self.size == 0:  # checks if the list is empty
            self.root = Node(d)  # if so we have to make a new node
            self.last = self.root
        else:  # other
            # it adds a new node in the beginning and makes the root node the next node
            new_node = Node(d, self.root)
            # it is a doubly linked list the root node prev pointer is connected to the new_node
            self.root.prev_node = new_node
            self.root = new_node  # the new node becomes the root
        self.size += 1  # incrementing to increase the size

    def find(self, d):
        this_node = self.root  # starting at the root node, which we call 'this node'
        while this_node is not None:  # iterating through the list using a while loop
            if this_node.data == d:  # a condition that checks if we find the data
                return d  # return the data if we find it
            else:
                this_node = this_node.next_node  # else we move on to the next node
            return None  # if we finish looping and we do not find the data we return None

    def remove(self, d):
        this_node = self.root  # start looking from the root
        while this_node is not None:  # while we are in a valid list
            if this_node.data == d:  # if we find the data
                # deleting the middle node
                if this_node.prev_node is not None:  # condition that checks if there is a previous node
                    if this_node.next_node is not None:  # condition that checks for a middle node
                        # bypassing the target node we are trying to delete
                        # setting its previous nodes next node to the next node
                        this_node.prev_node.next_node = this_node.next_node
                        # setting the next nodes previous node to the previous node
                        this_node.next_node.prev_node = this_node.prev_node
                    else:  # deletes last node
                        # changing the second to last node's next pointer to none
                        this_node.prev_node.next_node = None
                        self.last = this_node.prev_node
                else:  # deletes root node
                    self.root = this_node.next_node
                    this_node.next_node.prev_node = self.root
                self.size -= 1
                return True  # datta removed
            else:
                this_node = this_node.next_node
        return False  # data not found

    def print_list(self):  # print operation
        if self.root is None:
            return
        this_node = self.root
        print(this_node, end='->')

        # we are iterating through the list starting from the root, while it is a valid node
        while this_node.next_node is not None:  # checks if we made it back to the loop,
            this_node = this_node.next_node  # if not we continue to iterate
            print(this_node, end='->')
        print()

# test code


myDLL = DoublyLinkedlist()
x = [5, 9, 3, 8, 9]

for i in x:
    myDLL.add(i)

print(f"size= {str(myDLL.size)}")
myDLL.print_list()

myDLL.remove(8)

print(f"size= {str(myDLL.size)}")

print(myDLL.remove(15))
print(myDLL.find(15))
myDLL.add(21)
myDLL.add(22)
myDLL.remove(5)
myDLL.print_list()
print(myDLL.last.prev_node)
