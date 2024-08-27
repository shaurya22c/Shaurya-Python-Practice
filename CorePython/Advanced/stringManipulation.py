# string concatenation
# Using the + operator
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: Hello World

# Using join()
str_list = ["Hello", "World"]
result = " ".join(str_list)
print(result)  # Output: Hello World


# string slicing
s = "Hello, World!"
# Extracting "Hello"
print(s[:5])  # Output: Hello

# Extracting "World"
print(s[7:12])  # Output: World

# Reversing a string
print(s[::-1])  # Output: !dlroW ,olleH


# string formatting
# Using f-strings (Python 3.6+)
name = "Alice"
age = 30
print(f"Name: {name}, Age: {age}")  # Output: Name: Alice, Age: 30

# Using format()
print("Name: {}, Age: {}".format(name, age))  # Output: Name: Alice, Age: 30

# Using % operator
print("Name: %s, Age: %d" % (name, age))  # Output: Name: Alice, Age: 30





# string methods
s = "  Hello, World!  "

# Convert to lower case
print(s.lower())  # Output: "  hello, world!  "

# Convert to upper case
print(s.upper())  # Output: "  HELLO, WORLD!  "

# Remove leading and trailing whitespaces
print(s.strip())  # Output: "Hello, World!"

# Replace substring
print(s.replace("World", "Python"))  # Output: "  Hello, Python!  "

# Split into a list
print(s.split(","))  # Output: ['  Hello', ' World!  ']

# Find a substring
print(s.find("World"))  # Output: 8




# checking substrings
s = "Hello, World!"

# Check if "World" is in s
print("World" in s)  # Output: True

# Check if "Python" is not in s
print("Python" not in s)  # Output: True



# string reversal
s = "abcdef"
reversed_s = s[::-1]
print(reversed_s)  # Output: fedcba

# palindrome check
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello"))    # Output: False


# removing duplicates
def remove_duplicates(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)
    return ''.join(result)

print(remove_duplicates("aabbcc"))  # Output: abc


# anagram check
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))    # Output: False


# longest substring without repeating characters
def longest_unique_substring(s):
    char_set = set()
    left = 0
    result = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        result = max(result, right - left + 1)

    return result

print(longest_unique_substring("abcabcbb"))  # Output: 3 ("abc")
print(longest_unique_substring("bbbbb"))     # Output: 1 ("b")
