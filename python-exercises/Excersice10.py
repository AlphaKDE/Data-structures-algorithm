"""Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number"""

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

new_set = set(sample_list)  # create a set to remove all dupes

new_list = list(new_set)  # create a new list which has no duplicates

new_tuple = tuple(new_list)  # transform the list into a tuple

max_number = max(new_tuple)  # using the max function to find the max number

min_number = min(new_tuple)  # using the min function to find the min number

print(new_list)
print(new_tuple)
print(min_number)
print(max_number)
