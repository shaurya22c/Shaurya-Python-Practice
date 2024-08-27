# regex are used for string matching

# e.g. 1. check if email is correct or not

import re

pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"

user_input = input()

if re.search(pattern, user_input):
    print("valid email")

else:
    print("invalid email")

'''
Important methods in regex:

1. re.match(pattern, string) - check for match only at beginning of string
2. re.search(pattern, string) - search entire string for match

3. re.findall(pattern, string) 
pattern = r'\d+'
string = 'There are 3 cats, 4 dogs and 5 birds.'
print(re.findall(pattern, string))

output: ['3', '4', '5']

4. re.sub() - replace all occurences of pattern with specific replacement
pattern = r'\d+'
string = 'I have 2 apples and 3 oranges.'
print(re.sub(pattern, 'many', string))

output: I have many apples and many oranges.

5. re.split(pattern, string)

words = re.split(r'\s+', 'Split this sentence')
print(words)
words = ['Split', 'this', 'sentence']
'''