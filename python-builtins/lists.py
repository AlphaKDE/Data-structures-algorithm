"""list in python are the most general purpose data structure in python,
they are used for almost everything, they can be modified, they are a sequence types is sortable"""


# constructors for a list
x = []  # creating an empty list using bracket notation, which can than be populated with items
# crating list with list comprehension ###very important when you want a list with values that  you can filter
y = [item for item in range(10) if item > 4]
print(y)  # will only output the list [5,6,7,8,9]
z = list()  # using the list function to create an instance of the list class

# string slicing using bracket notation [start:end+1:step] if you do not declare a start it defaults to the beginning,
# end defaults to the end and step defaults to 1

x = 'computer'
# only printing the second item through the 4th item it is NOT inclusive
print(x[1:4])
# we can use th python slice function as well to slice a string, slice(start,end,step) which can be indexed later on
y = slice(1, 4)
print(x[y])


# we can concatinate strings using the + symbol

x = [2, 3, 4]
y = [5, 6, 7]
print(x + y)  # this will give you [2,3,4,5,6,7] the same goes for tuples

# checking membership in tuples and list
x = [1, 2, 3, 4]
# checks to see if 5 is in 5 and return a boolean value, true if in x false if not in x.
print(5 in x)
# checks to see if 5 is NOT in x, true if 5 isnt in x and false if 5 is in x.
print(5 not in x)

# Iterating through items in a sequence.
x = [7, 8, 3]
for item in x:
    print(item)  # this will return each item in the list seperately

# We could also check for the index of an item using the enumerate function

x = [7, 8, 3]
for index, item in enumerate(x):
    print(index, item)  # this will print both the index and the item of the list

# working with number of items
X = [7, 8, 9, 10]
print(len(x))  # the len function returns the lenght of a list in this case 4

min(x)  # returns the minimum number of a list
max(x)  # returns the max

sum(x)  # sums the whole list
print(sum(X[:2]))  # string slicing can be used to sum part of the list

# sorted function
x = 'bug'
sorted(x)  # returns a new list in sorted order, it is done using the ascii standard so letters can be sorted as well
# we can sort a list using a specifc item using the lambda function
sorted(x, key=lambda k: k[1])

# unpacking
x = ['pig', 'cow', 'horse']
a, b, c = x  # we are unpacking each item in the list,

print(a, b, c)  # will print out pig,cow,horse

# important list functions::

# delete function

x = [5, 6, 7, 8]
del (x[1])  # deletes the second item in the list
del (x)  # deletes the whole list

# append function

x = [5, 45, 6, 4]
x.append(7)  # we are adding the 7 to the end of the list

# extend function, a diferent way to concatinate two lists
x = [5, 6]
y = [7, 8]

x.extend(y)
print(x)  # x will now be [5,6,7,8]

# insert function
x = [5, 6, 7, 8]
# inserts the list ['a','b'] in the first index and shifts the others
x.insert(1, ['a', 'b'])
print(x)

# pop function
x = [5, 6, 7, 8]
x.pop()  # removes the last item in the list

# remove function
x = [5, 6, 7, 8]
x.remove(5)  # removes the first occurance of an item

# reverse function
x = [5, 6, 7, 8]
x.reverse()
print(x)  # this is simply reversing the order of an item

# sort functions
x = [5, 6, 7, 8]
x.sort()  # sorts in place, which means that it does not make a new list
x.sort(reverse=True)  # a descending sort
