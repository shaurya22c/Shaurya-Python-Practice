# syntax: sequence[start:stop:step]
# Negative Indices: Count from the end

# Creating a list
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Slicing from index 2 to 5 (excluding 5)
print(my_list[2:5])  # Output: [2, 3, 4]


# Creating a string
my_string = "Hello, World!"
# Slicing from index 7 to the end of the string
print(my_string[7:])  # Output: "World!"


# Creating a list
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Slicing from the beginning to index 5 (excluding 5)
print(my_list[:5])  # Output: [0, 1, 2, 3, 4]
# Slicing from index 5 to the end of the list
print(my_list[5:])  # Output: [5, 6, 7, 8, 9]



# Creating a list
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Slicing from the second last element to the end of the list
print(my_list[-2:])  # Output: [8, 9]
# Slicing the entire list except the last element
print(my_list[:-1])  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8]



# Creating a list
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Slicing every second element from index 1 to 8 (excluding 8)
print(my_list[1:8:2])  # Output: [1, 3, 5, 7]


# Creating a list
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Reversing the list
print(my_list[::-1])  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


# Creating a list
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Slicing from index 1 to 8 (excluding 8) with a step of 2
print(my_list[1:8:2])  # Output: [1, 3, 5, 7]
# Slicing from the end to the start with a step of -2
print(my_list[::-2])  # Output: [9, 7, 5, 3, 1]


# Creating a list
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Copying the entire list
copy_list = my_list[:]
print(copy_list)  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]



# Creating a string
my_string = "Hello, World!"
# Extracting "Hello"
print(my_string[:5])  # Output: Hello
# Extracting "World"
print(my_string[7:12])  # Output: World
# Extracting every second character
print(my_string[::2])  # Output: Hlo ol!




def first_half(seq):
    return seq[:len(seq) // 2]
# Testing with a list
print(first_half([1, 2, 3, 4, 5, 6]))  # Output: [1, 2, 3]
# Testing with a string
print(first_half("abcdef"))  # Output: "abc"
