"""
three types of methods in Python:

instance methods  most used

class methods

static methods

"""

"""
Methods act as an interface between a program and the properties of a class in the program.

These methods can either alter the content of the properties or use their values to perform a particular computation.

"""

class Employee:
    # defining the initializer
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    def tax(self):
        return (self.salary * 0.2)

    def salaryPerDay(self):
        return (self.salary / 30)


# initializing an object of the Employee class
Steve = Employee(3789, 2500, "Human Resources")

# Printing properties of Steve
print("ID =", Steve.ID)
print("Salary", Steve.salary)
print("Department:", Steve.department)
print("Tax paid by Steve:", Steve.tax())
print("Salary per day of Steve", Steve.salaryPerDay())


"""
Overloading refers to making a method perform different operations based on the nature of its arguments.

methods cannot be explicitly overloaded in Python but can be implicitly overloaded.

In order to include optional arguments, we assign default values to those arguments rather than creating a duplicate method with the same name. If the user chooses not to assign a value to the optional parameter, a default value will automatically be assigned to the variable.
"""

class Employee:
    # defining the properties and assigning them None to the
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department

    # method overloading
    def demo(self, a, b, c, d=5, e=None):
        print("a =", a)
        print("b =", b)
        print("c =", c)
        print("d =", d)
        print("e =", e)

    def tax(self, title=None):
        return (self.salary * 0.2)

    def salaryPerDay(self):
        return (self.salary / 30)


# cerating an object of the Employee class
Steve = Employee()

# Printing properties of Steve
print("Demo 1")
Steve.demo(1, 2, 3)
print("\n")

print("Demo 2")
Steve.demo(1, 2, 3, 4)
print("\n")

print("Demo 3")
Steve.demo(1, 2, 3, 4, 5)


"""
If we redefine a method several times and give it different arguments, Python uses the latest method definition for its implementation.

under the hood, overloading saves us memory in the system. Creating new methods is costlier compared to overloading a single one.
"""
