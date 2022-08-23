"""Binary search trees are a critical programming structure, it is extremly fast, for example with as few as 30 guesses
you would be able to find a piece of data in a tree with 10 million nodes,(by reducing it in half after each guess) trees are used for work hierarchy, but its most important
benefit is its speed in finding data."""

# in a binary tree each node may have up to 2 child nodes, it cannot exceed 2, if so it is not a binary tree
# in a binary tree each node is greater than every single node in its left subtree, and each node is less than every single node in its right sub tree

# standard operations- # most operations in a bst use recursion because we call the same function(recurvise case) using the same parameter until we find what we want(condition)

# INSERT O(logn)- insert data in a tree:
# always start at the root when we are doing an insertions, but we do not insert it as a root we use it for comparison to see where the node goes.
# if the node we are insert is less than the root we must send it to the left subtree if it is greater we send it to the right subtree,until it is a leaf node


# FIND O(logn)- finding a pice of data in a tree:
# we start at the root, and compare if the data is less than the root node we go down left subtree if it is greater we go down the right subtree
# and return the data if not we return false

# DELETE  O(logn) - remove a piece of data in a tree: 3 possible cases we must consider
# 1- the node we want to delete is a leaf node:
# in the case of a leaf node we can just delete that node since it will be at the bottom of the tree and have no impact on the tree

# 2- the node has one children:
# if the node has one child we must promote the child to be in the position of the node we want to delete

# 3 - the node had 2  children:
# we must find the next higher node and replace it with the node we want to delete


# GET_SIZE- tells us how many nodes are in a tree:

# returns the number of nodes.. works recursively
# size = 1(rootnode) + size(left subtree) + size(right subtree)

# TRAVERSALS- walking through the tree node by node- there are multiple ways to traverse a tree(AKA multiple algorithms we can use )
# traversal algorithms:
# - preorder traversals -  starts at the root, we visit the root before we visit the root subtrees

# - inorder traversal- starts at a left mode node leaf usually to provided sorted order , than we visit the root between visiting the root's subtrees, it gives values in sorted order

# - level traversal- We visit all nodes at a perticular level in the tree before visiting the node at a deeper level

# -post order traversal- we start at the root first we traverse the left subtree than we traverse the nodes right subtree

# python Implementation

class Tree:
    # sets three atributes, the data, the left subtree and the right subtree
    def __init__(self, data, leftSubtree=None, rightSubtree=None):
        self.data = data
        self.leftSubtree = leftSubtree
        self.rightSubtree = rightSubtree

    def insert(self, data):
        if self.data == data:  # checks to see if the data is already in the tree
            return f"{False} you cannot enter a duplicate value"  # duplicate
        elif self.data > data:  # if the data is greater, we must insert it in the left subtree
            if self.leftSubtree is not None:  # checks to see if we have a valid left subtree to insert it in
                # using recursion on the insert function
                return self.leftSubtree.insert(data)
            else:  # if we do not have a left subtree
                self.leftSubtree = Tree(data)  # we must make a new subtree
                return True  # data was inserted
        else:  # we re checking if self.data is less than data, we must insert it in the right subtree
            if self.rightSubtree is not None:  # and we have a valid right subtree to insert the data in
                # using recursion again to insert the data
                return self.rightSubtree.insert(data)
            else:  # if we do not have a rightsubtree
                self.rightSubtree = Tree(data)  # we must make a right subtree
                return True  # the data was inserted

    def find(self, data):
        if self.data == data:
            return data  # we find the data
        elif self.data > data:  # if the data we are looki g for is greater than the current node we must descend down the left subtree
            if self.leftSubtree is None:  # if the left subtree is none than the data is not found
                return False  # return false
            else:
                # using recursion to loop through the data again until we find it
                return self.leftSubtree.find(data)
        elif self.data < data:  # if the data we are looking for is less than the current node, we must descend down the right subtree
            if self.rightSubtree is None:  # if there is not rightsubtree
                return False  # we return false because data is not found
            else:
                # we call the find function recursively to loop throught again.
                return self.rightSubtree.find(data)

    def get_size(self):
        if self.leftSubtree is not None and self.rightSubtree is not None:
            # using recursion to continously call the getsize function
            return 1 + self.leftSubtree.get_size() + self.rightSubtree.get_size()
        elif self.leftSubtree:  # if we only have the left subtree
            return 1 + self.leftSubtree.get_size()  # the 1 being added is the root node
        elif self.rightSubtree:  # if we only have the right subtree
            return 1 + self.rightSubtree.get_size()
        else:  # if we only have the root node
            return 1

    #traversals-- preorder and inorder

    def preorder(self):
        if self is not None:  # checks to see if the node we are in is not node
            # printing the values before we descend the two subtrees
            print(self.data, end=' ')
            if self.leftSubtree is not None:
                # we are calling the preorder function recursively until we reach a none node
                self.leftSubtree.preorder()
            if self.rightSubtree:  # than once we reach a none node we continous down the right subtree
                # calling the preorder recursively until we reach a none left none
                self.rightSubtree.preorder()

    def inorder(self):
        if self is not None:  # checks to see if we are in a node
            if self.leftSubtree is not None:  # if we have a valid left subtree
                self.leftSubtree.inorder()
            # printing the value in between the the subtrees
            print(self.data, end=' ')
            if self.rightSubtree is not None:
                self.rightSubtree.inorder()
        # -post order traversal- we start at the root first we traverse the left subtree than we traverse the nodes right subtree

    def postorder(self):  # post order
        if self is not None:  # checks to see if we are in a valid node
            if self.leftSubtree is not None:  # if we have a left node to traverse
                # we visit the left node and call it recursively until we we done with the left subtree
                self.leftSubtree.postorder()
            if self.rightSubtree is not None:
                self.rightSubtree.postorder()
                print(self.data, end=' ')


# test code
myTree = Tree(7)
myTree.insert(9)

x = [15, 10, 2, 12, 3, 1, 13, 6, 11, 4, 14, 9]

for i in x:
    myTree.insert(i)

for i in range(16):
    print(myTree.find(i), end=' ')

print('\n', myTree.get_size())

myTree.preorder()
print()

myTree.inorder()
print()

myTree.postorder()
print()
