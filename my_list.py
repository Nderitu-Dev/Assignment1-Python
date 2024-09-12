# creating an empty list
my_list = []

# appending elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#inserting the value 15 at second position
my_list.insert(1, 15)

#extending my list
my_list.extend([50, 60, 70])

# Removing the last element
my_list.pop()

#sorting the list
my_list.sort()

# finding and printing the index of the value 30
index_of_30 = my_list.index(30)
print("index of 30:", index_of_30)

# printing final output
print(my_list)