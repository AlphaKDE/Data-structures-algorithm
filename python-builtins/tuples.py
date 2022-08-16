"""tuples are liked list except they are immunable, which means you cannot modify them they are useful for fixed data
they are much faster items than a list in, they are also sequence types which means all 
functions used in a list can also be used in a function """

# creating tuples


x = ()  # empty tuple
x = (1, 2, 3, 5)
x = 1, 2, 3, 5  # we can remove the parenthesis python will still recognize it as a tuple
x = 5,  # for single items we must add the comma to be a tuple
list1 = [2, 4, 5]
y = tuple(list1)  # the list is now turned into a tuple

# tuples are immunable,however member items can be changed,

x = ([1, 2], 3)
# this will go inside the list inside the tuble and delete the second item aka the '2'
del (x[0][1])
print(x)  # the new tuple is ([1],3)

# concatenating two tuples we cannot use th append method
y = (1, 2,)
y += 4,  # this is like y = y + (4,) it adds 4 at the end of the tuple
