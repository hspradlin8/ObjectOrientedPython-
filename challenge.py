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

