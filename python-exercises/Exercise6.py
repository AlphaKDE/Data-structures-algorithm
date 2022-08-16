"""Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set"""

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

# gets the intersection of the two list and places inside a set
intersections = first_set & second_set


# brute force:

y = list(intersections)  # changes the set to a list item for easy access

first_set.remove(y[0])
first_set.remove(y[1])
first_set.remove(y[2])


# loop- here we do not need to use the list function to transform the set into a list we can loop it as is:

print(first_set)

y = intersections
for item in y:
    first_set.remove(item)

print(first_set)
