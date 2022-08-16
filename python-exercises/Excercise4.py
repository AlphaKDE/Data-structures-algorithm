"""Exercise 4: Count the occurrence of each element from a list
Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element."""

# brute force
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
occurancedict = {}  # initialize an empty dictionary
occurancedict[11] = sample_list.count(11)
occurancedict[45] = sample_list.count(45)
occurancedict[8] = sample_list.count(8)
occurancedict[23] = sample_list.count(23)
occurancedict[45] = sample_list.count(45)
occurancedict[89] = sample_list.count(89)

print(occurancedict)

# loop
occurancedict = {}
for item in sample_list:
    # uses count method to count the items as i am iterating the list
    occurancedict[item] = sample_list.count(item)
print(occurancedict)

# better loop?
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]


count_dict = dict()
for item in sample_list:
    if item in count_dict:  # checks to see if the item is in the dictiorny
        count_dict[item] += 1  # if it is add one to it
    else:
        count_dict[item] = 1  # if it is not set it to one

print(count_dict)

# function


def countOcc(list: list):
    occurancedict1 = {}
    for item1 in list:
        occurancedict1[item1] = list.count(item1)
    return occurancedict1


print(countOcc([11, 45, 8, 11, 23, 45, 23, 45, 89]))
