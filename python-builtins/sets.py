"""sets are used in python to store unique items, it has very fast items compared to lists, in a set to find an item pythong hashes it
which means we can find the item instantly we do not have to loop through the item , it is great for checking memberships 
it comes with math sets operations like (union,intersect) """

# creating sets

x = {3, 5, 3, 5}
print(x)  # python will remove the duplicates and only print out  {3,5}
x = set()  # creating an empty set
list1 = [2, 3, 4, 5]
# turns list one into a set, so if they list had any dupes in it python would remove it
z = set(list1)

# set operations
x = {3, 8, 5}
x.add(7)  # this will add 7 to the set

x.remove(3)  # this will remove the number 3 from the set

len(x)  # provides us with the lenght of the set in this case it would be 3 because we added 7 and removed a 3

# similar to a list we can check for memebership using the in and not in keywords
print(5 not in x)

print(x.pop(), x)  # here we are using the pop method, since a set is unordered we will be removing a random item from the set, which is why we want to print the value removed and the new set

x.clear()  # deletes all the items from a set.

# Mathematical set operations
# intersection(AND) s1 & s2
# Union(OR) set1 | set2
# symmetric difference(XOR): set1^set2
# difference (in set1 but not in set2): set1-set2
# subset(set2 contains set1): set1 <= set2
# superset(set1 contains set2): set1>= set2
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 & s2)
print(s1 | s2)
print(s1 ^ s2)
print(s1 - s2)
print(s1 <= s2)
print(s1 >= s2)
