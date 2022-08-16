"""Exercise 3: Slice list into 3 equal chunks and reverse each chunk"""

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

chunk_1 = sample_list[0:3]

chunk_2 = sample_list[3:6]

chunk_3 = sample_list[6:]

chunk_1.reverse()
chunk_2.reverse()
chunk_3.reverse()

print(chunk_1)
print(chunk_2)
print(chunk_3)


# using a for loop


sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list ", sample_list)

length = len(sample_list)
# we have a lenght of 9 items for 3 equal parts we need to divide by 3
chunk_size = length // 3
start = 0
end = chunk_size

# run loop 3 times


for i in range(3):
    # get indexes
    indexes = slice(start, end)

    # get chunk
    list_chunk = sample_list[indexes]
    print("Chunk ", i, list_chunk)

    # reverse chunk
    print("After reversing it ", list((reversed(list_chunk))))

    start = end  # updates after each iteration from 0 to 3 to 6
    end = end + chunk_size  # updates after each iteration from 3 to 6 to 9
