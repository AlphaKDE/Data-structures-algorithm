"""A Min-Heap is a complete binary tree in which the value in each internal node is smaller than or equal to the values in the children of that node. 
Mapping the elements of a heap into an array is trivial: if a node is stored at index k, then its left child is stored at index 2k + 1 and its right child at index 2k + 2 for 0 based indexing and 
for 1 based indexing the left child will be at 2k and right child will be at 2k + 1."""

# a min heap is the opposite of a max heap, the first index will always be the minimum number and the last index will always be the maximum number
# it has all the operations that a max heap has


class minHeap:
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
            min = self.heap.pop()  # the last item can now be popped off
            self.__bubbleDown(1)  # bubble down the first item
        elif len(self.heap) == 2:  # if the list has exactly 2 items one that means one of the items is the zeros index that we arent using
            # therefore the item retrieved from the pop function will be the max
            min = self.heap.pop()
        else:
            min = False
        return min
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
        elif self.heap[index] < self.heap[parent]:
            # if it is less  than its parent than we call the swap function on it
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


# test cases
my_minHeap = minHeap([95, 3, 21])
my_minHeap.push(10)
my_minHeap.push(2)
print(my_minHeap)
