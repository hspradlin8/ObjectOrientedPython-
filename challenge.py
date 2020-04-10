# 1. Make a new class named Student.
# Give it an attribute name and put your own name, as a string, into the attribute.


class Student:
    name = "Heidi"

# 2.Now, make an instance of your class named me.
# Then print() out the name attribute of your instance.


me = Student()
print(me.name)

# 3. Alright, I need you make a new method named feedback.
# It should take an argument named grade. Methods take arguments just like functions do.
# You'll still need self in there, though.
# If grade is above 50, return the result of the praise method.
# If it's 50 or below, return the reassurance method's result.


class Student:
    name = "Your Name"

    def praise(self):
        return "You inspire me, {}".format(self.name)

    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)

    def feedback(self, grade):
        if grade > 50:
            return "You inspire me, {}".format(self.name)
        return "Chin up, {}. You'll get it next time!".format(self.name)


# 1 I've made you a super-simple Inventory class that would let someone store items in it. Not the most useful class,
# but we'll build something better in a few videos.
# For now, though, I need you to create a new class, SortedInventory that should be a subclass of Inventory.
# You can just put pass in the body of your class for this step.

# 2 Now override the add_item method. Use super() in it to make sure the item still gets added to the list.

# 3 Sorted inventories should be just that: sorted. Right now, we just add an item onto the slots list whenever
# our add_item method is called. Use the list.sort() method to make sure the slots list gets sorted after an item is added.
# Only do this in the SortedInventory class.

class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)
 # 1, 2,3


class SortedInventory(Inventory):
    def add_item(self, item):
        super().add_item(item)
        self.slots.sort()

# Alright, here's a fun task! Create a function named combiner
# that takes a single argument, which will be a list made up of strings and numbers.
# Return a single string that is a combination of all of the strings in the list and then the sum of all of the numbers.
# For example, with the input ["apple", 5.2, "dog", 8], combiner would return "appledog13.2". Be sure to use isinstance to solve this as I might try to trick you


def combiner(value):
    # Variable to store concatenated strings
    Strings = ""
    # Variable to store added numbers
    Nums = 0
    # Loop through the values in value
    for val in value:
        # Test to see if val is of type float or string
        if isinstance(val, (int, float)):
            Nums += val
        elif isinstance(val, str):
            Strings += val
    # finalValue concatenates the final Strings and Nums variables. Nums is converted to a string value to allow proper concatenation
    finalValue = Strings + str(Nums)
    return finalValue
