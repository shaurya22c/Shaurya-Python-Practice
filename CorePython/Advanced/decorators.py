# Decorator is a function that takes another function as argument and returns a function

def decorator(func):
    def wrapper():
        print("Transaction started")
        func()
        print("Transaction completed")
    return wrapper

@decorator
def transaction_logic():
    print("Transaction in process")

transaction_logic()