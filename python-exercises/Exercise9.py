"""Exercise 9: Get all values from the dictionary and add them to a list but don't add duplicates"""


# brute force??
speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44,
         'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

# takes all the values from the dictionary and add it into a set, python will remove all dupes
set1 = set(speed.values())

list1 = list(set1)  # uses the list function to turn the set into a list

print(list1)
