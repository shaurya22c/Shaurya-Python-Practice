# metaclasses allow us to control the creation and behavior of classes
# class define behavior of objects, while metaclasses define behavior of classes

# for e.g. we want to enforce classes to have particular attribute:

# defining meta class
class AttributeEnforceMeta(type):
    # method to create class based on our logic (enforce attributes)
    def __new__(cls, name, bases, dct):
        if 'required_attribute' not in dct:
            raise AttributeError(f"{name} class must have 'required_attribute'")
        return super().__new__(cls, name, bases, dct)

class CorrectClass(metaclass=AttributeEnforceMeta):
    required_attribute = 42

class IncorrectClass(metaclass=AttributeEnforceMeta):
    pass # This will raise an error