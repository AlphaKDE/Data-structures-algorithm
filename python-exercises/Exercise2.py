"""write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list 
"""


list1 = [34, 54, 67, 89, 11, 43, 94]

# the pop function return the value of the item that was taken out of the list so we set it to the value x
x = list1.pop(4)
# the insert function takes two parameters the first is the index you wan to insert something at and the second is the actual something
list1.insert(2, x)

list1.append(x)  # using the append function to add x to the end of the list

print(list1)
