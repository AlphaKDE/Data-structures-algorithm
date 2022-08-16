"""given 2 list l1 and l2, write a program to creata a third list l3 by picking  odd-index 
elements from l1 and even-index elements from list l2"""

# 0 odd 1 even
l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]


def OddEven(x, y):
    l3 = []  # initializes the new list
    # using enumerate to get access to the index and items seperately
    for index, item in enumerate(l1):
        if index % 2 == 1:  # a condition that checks for the condition if the index is odd
            l3.append(item)  # append method to add the item to l3
    for index, item in enumerate(l2):
        if index % 2 == 0:  # checkf if the index is even
            l3.append(item)
    return l3


print(OddEven(l1, l2))
