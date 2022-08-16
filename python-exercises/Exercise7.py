"""Exercise 7: Checks if one set is a subset or superset of another set. If found, delete all elements from that set"""
first_set = {27, 43, 34}

second_set = {34, 93, 22, 27, 43, 53, 48}

if first_set <= second_set:
    first_set.clear()
if second_set <= first_set:
    second_set.clear()

print("first set", first_set)
print("second set", second_set)
