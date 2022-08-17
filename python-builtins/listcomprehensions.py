"""python list comprehensions are a great way to create new list that contain specific 
and precise data depending on what algorithm you are implimenting
SYNTX: [expression for item in iterable if condition == True]"""


import random

under_10 = [x for x in range(10)]  # outputs a list [0,1,2,3,4,5,6,7,8,9]

print('under_10:' + str(under_10))

# using a list comprehension to get a new list of the squares of the under_10 list
squares = [x**2 for x in under_10]
print("suares:", squares)

# we  also use a condional statement to only had the odd numbers in the list
odds = [x for x in range(10) if x % 2 == 1]
print("odds:", odds)

# getting multiples of 10
ten_x = [x * 10 for x in range(10)]
print('ten_x:', ten_x)

# getting all the numbers from a string
s = 'I love 2 go t0 the store 7 times a w3ek'
# checking to see if the x is a number
numbers = [x for x in s if x.isnumeric()]

print(f"nums : {''.join(numbers)}")

# getting the index of a list
names = ['cosmo', 'pedro', 'Anu', 'Ray']

# gives you the index of the item
idx = [index for index, item in enumerate(names) if item == "Anu"]

print(f"idx={(idx[0])}")

# deleting an item from a list
letters = [x for x in 'ABCDEF']
random.shuffle(letters)
letrs = [a for a in letters if a != 'C']

print(f"letters before condition {letters}, after condition {letrs}")

# if/else in a list comprehension- both conditions must come before the iteration
nums = [5, 3, 10, 18, 6, 7]
# if x is even we leave it as is, else we multiply it by 10
new_list = [x if x % 2 == 0 else 10*x for x in nums]

print(f"{nums}, {new_list}")
