'''
Generators in python are like iterables which don't store all values in memory at once.
Instead they generate values when you require and yield them one by one
Use yield keyword with generators
Hence Generators are memory efficient
They are generally used when dealing with large files
'''

# use of generator to efficiently read large log file
def parse_large_log_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if "ERROR" in line:
                yield line.strip()

for error_line in parse_large_log_file('server.log'):
    print(error_line)

'''
generator function reads each line of the file, checks if it contains the word "ERROR," and yields it. This approach allows you to process each line as it's read, without ever needing to hold the entire file in memory.
'''