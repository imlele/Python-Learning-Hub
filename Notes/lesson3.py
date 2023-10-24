# A Class is a custom data type
# A class is a prototype for an object
# An object is a structured piece of data, an instance of a class
# Ex: int is a class, 5 is an object
# Ex: str is a class, "hello" is an object
# Ex: Person is a class, bob is an object

# A class has 2 things:
# 1. Attributes (data)
# 2. Methods (functions)

# Attributes (also called fields), are the internal representation of data
# Methods are functions, which represent actions, an object can perform

# Example class
class Person:
    name: str
    age: int

    def introduce(self):
        print(f"my name is {self.name} and I am {self.age} years old")

    def change_name(self, new_name):
        self.name = new_name

# Initialize
bob = Person()
bob.name = "Bob"
bob.age = 25

print(bob.name)

bob.introduce()
bob.change_name("John")

# However, what if we forget to initialize all attributes?
# It takes too many lines of code.
# We can use a constructor instead.

class Person:
    name: str
    age: int

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"my name is {self.name} and I am {self.age} years old")

    def change_name(self, new_name):
        self.name = new_name

bob = Person("Bob", 25)
# Now, bob is initialized in 1 line, and its name and age are set
# in the constructor

# How initialization happens:
# 1. Python creates a new, empty instance of Person
# 2. The arguments passed to the constructor ("Bob", 25) are collected
# 3. The magic method "__init__" is called, and
#    python passes "Bob", 25 to it
# 4. The __init__ sets the attributes of the object to
#    the values passed to it (and does whatever we want it to do)
# 5. The Person("Bob", 25) constructor call returns the
#    instance of Person, and the program can continue

# If the __init__ method is not defined, python will use
# the default one, which does nothing:
def __init__(self):
    pass

# If an init method is defined, it must be called
# with the correct number of arguments
# If it is not called properly, python will throw an error
kate = Person() # TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'


# Now, every instance of Person has a name and an age
bob.introduce()
bob.change_name("John")
bob.introduce()


# Now, instead of thinking of our program in terms of functions and steps,
# We can think of it in terms of objects and how they interact with each other

# Lets create a prototype for an online store!

# Import type List, to use to define fields. (We will talk about imports later)
from typing import List

class Item:
    name: str
    price: float
    description: str
    discount: float
    
    def change_name(self, new_name):
        pass
        # self.name = new_name

    def change_price(self, new_price):
        pass

    def set_discount(self, discount):
        pass

    def get_discount_price(self):
        return self.price * self.discount


class InventoryItem:
    item: Item
    quantity: int

    def get_total_price(self):
        pass


class Inventory:
    items: List[InventoryItem]

    def add_item(self, item: InventoryItem):
        pass

    def remove_item(self, item_name):
        pass

    def change_quantity(self, new_inventory_item):
        pass

    def get_total_price(self):
        pass
    

class User:
    name: str
    email: str
    inventory: Inventory
    password: str # :)

    def change_email(self, new_email):
        pass

    def login(self, password):
        pass

    def change_password(self, new_password):
        pass

    def checkout(self):
        pass

# There are many ways to design classes! Many would work,this is just one way.
# However, some ways of designing classes are considered "better"
# than others. This is the topic of Software Design!

# We can now do all this:
item = Item()
item.name = "Apple"
item.price = 1.99
item.description = "A red apple"

item2 = Item()
item2.name = "Orange"
item2.price = 2.99
item2.description = "A juicy orange"

inventory_item = InventoryItem()
inventory_item.item = item
inventory_item.quantity = 10

inventory_item2 = InventoryItem()
inventory_item2.item = item2
inventory_item2.quantity = 5

inventory = Inventory()
inventory.add_item(inventory_item) # right now, does nothing
inventory.add_item(inventory_item2)

# HOMEWORK!
# Take the classes above (or your own classes you created in class),
# and implemented the methods (replace "pass" with actual code)
