"""Dictionaries in python are key value pairs, they are an associative array, like a hashmap in java 
which means you can associate various things with each other and access them later for problem solving
they are unordered, they cannot be sorted"""


# creating a list dictionary

x = {}  # for creating an empty dictionary

# sets up a key value pair to associate each value to an object
x = {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7}
print(x)

# we can use the dict function to turn a list of tuples into a dictionary
x = dict([('pork', 25.3), ('beef', 33.8), ('chicken', 22.7)])

print(x)

# another way to create a dictionary
x = dict(pork=25.2, beef=33.8, chicken=22.7)
print(x)

# dictionary operations

x = {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7}
# we can add or update values in a dictionary using bracket notaion
x['shrimp'] = 38.2  # this adds shrimp to the dictionary and set its value to 8 if it is not in there, if it is in the dictionary it would update its value

# deleting an item
del (x['shrimp'])

# getting the lenght
len(x)  # will tell you how many key value pairs are in the dictionary
x.clear  # deletes all the items in the dictionary.
del (x)  # deletes the entire dictionary.

# accessing keys and values in a dictionary
y = {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7}
print(y.keys())  # returns a list of the keys
print(y.values())  # returns the values
print(y.items())  # returns the items in a list of tuples

# checking for membership

# this only looks for keys it would not make a difference if we did "y.keys()"
print('beef ' in y)

# checks for membership in the values, here we have to use the y.values
print('clams' in y.values())

# iterating a dict- thes items are in random order when we iterate python will give it to you in whatever order it wants.

for key in y:
    # here we want two values the key itself and the value which is obtained using bracket notation
    print(key, y[key])

# we can also iterate using the .items method using 2 variables in case we want to do things with the dictionary in the loop
for k, v in y.items():  # y.items returns a tuple therefore we are mapping k and v to the two items returneds
    print(k, v)
