""" A max heap is a complete binary tree wher every node is <= to its parent, the highest number 
can be instantly removed and used because we can simply just pop it from the tree because it will always be
the firs parent node"""

# Max heaps are extrememly fast, you can insert an item in O(logn)
# get the Max in O(1)
# remove Max in O(logn)

# for 1 base index:to access the left child of a parent node we multiply the parent nodes index by 2(I*2), and to access its right child we multiply by 2 and add 1(I*2+1),
# for 0 base index:to access the left child of a parent node we multiply the parent nodes index by 2 and add 1 (2*I+ 1), and to access its right child we multiply by 2 and add 2 (2*I+2),

# to make implimentation easiser we start indexing from index 1 instead of standard 0.

# operations

# push(insert): the push operation has two parts
# 1 - add the value at the end of the array
# 2- float it up to its proper position(we must code this, psedocode: if the value is greater than its parent node we must swap them  )

# peek(get max): just return the value at index #1,

# pop(remove max): the pop operation has four parts
# 1- swap the max with the node at the end of the array() so our tree remains intact.
# 2- now we can remove the last node without affecting the heap,
# 3 Bubble Down the item at index 1 to its proper position( we must code this, we must compare node swapped to the right and left nodes if it is less we must swap them, and keep comparing until we get it in position)
# 4 return the max

# python Implimentation for max heap


class maxHeap:
    # creating a new list we have the option to pass in a list of items, if not it defaults to an empty heap
    def __init__(self, items=[]):
        super().__init__()
        # placing a zero in the very first element because we start our indexing at one for the max heap
        self.heap = [0]
        for item in items:  # if we are given a list of items we iterate through it and add them one at a time to the heap
            # adding the items one at a time to the end of the list
            self.heap.append(item)
            # float it up to its proper position using the push operation
            self.__floatUp(len(self.heap) - 1)

    def push(self, data):  # push operation we append the data given and add it to the list
        self.heap.append(data)
        # we use the float up magic method to move the data to the top of the list
        self.__floatUp(len(self.heap)-1)

    def peek(self):  # peek operation,
        if self.heap[1]:  # checking to see if we have a max item in the heap
            return self.heap[1]  # if so return
        else:
            return False  # if not return false

    def pop(self):  # pop operation
        if len(self.heap) > 2:  # if the list has more than 2 items
            # than we will swap the max with the last item
            self.__swap(1, len(self.heap) - 1)
            max = self.heap.pop()  # the last item can now be popped off
            self.__bubbleDown(1)  # bubble down the first item
        elif len(self.heap) == 2:  # if the list has exactly 2 items one that means one of the items is the zeros index that we arent using
            # therefore the item retrieved from the pop function will be the max
            max = self.heap.pop()
        else:
            max = False
        return max
# utility functions

    def __swap(self, i, j):
        # we pass it two indeces and swap them
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # the floatup funcion recieves the index of the item we want to float up
    def __floatUp(self, index):
        parent = index // 2  # we know that the parent index will be the given index divided by 2
        if index <= 1:  # if the index is less than or equal to one that means there is nothing to float up
            return
        # otherwise we will compare it to its parent
        elif self.heap[index] > self.heap[parent]:
            # if it is greater than its parent than we call the swap function on it
            self.__swap(index, parent)
            # than we call the floatup function recursively
            self.__floatUp(parent)

    def __bubbleDown(self, index):
        left_child = index * 2  # the index of the left child
        right_child = index * 2 + 1  # the index of the right child
        largest = index  # the largest index

        # if the item we are bubbling is less than its left child
        if len(self.heap) > left_child and self.heap[largest] < self.heap[left_child]:
            largest = left_child  # we swap the position for the largest to be the left_child now
        # if the item we are bubbling down is less than the right child
        if len(self.heap) > right_child and self.heap[largest] < self.heap[right_child]:
            largest = right_child  # we swape the postition for the largest to be the right_child
        if largest != index:
            # if there is swapping to be done we will call the swap function on the item we are bubbling(index) with the larger of the two
            self.__swap(index, largest)
            # call the bubble down function recursively until it reaches its proper position
            self.__bubbleDown(largest)

    def __str__(self):
        return str(self.heap)


# test code

my_maxHeap = maxHeap([95, 3, 21])

my_maxHeap.push(10)  # pushing 10 into the heap
my_maxHeap.push(100)
print(my_maxHeap)

print(my_maxHeap.pop())
print(my_maxHeap.peek())
