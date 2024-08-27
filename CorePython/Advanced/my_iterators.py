'''
Iterator is an object that allows you to traverse all elements of a collection
Iterator object implements two methods:

__iter__() : returns iterator object itself
__next__() : returns next value from collection

if you want to create custom iterator, you need to override these two methods based on your logic
'''

class EvenNumbers:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.max_value:
            raise StopIteration
        else:
            even_number = self.current
            self.current += 2
            return even_number

even_numbers = EvenNumbers(10)

for num in even_numbers:
    print(num)