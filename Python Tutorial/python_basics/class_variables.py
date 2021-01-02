class Employee:

    num_of_emps = 0
    raise_amount = 1.04 #class variable which can be accessed through Employee.raise_amount or self.raise_amount
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1 #accessing a class variable and incremented everytime an instance is created since __init__ is called upon
    
    
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) #accessing a class variable




emp_1 = Employee("Amay", "Jain", 50000)
emp_2 = Employee("Test", "User", 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.__dict__)

Employee.raise_amount = 1.05 #use class_name.class_variable to change value of class variable for the whole class and instances
emp_1.apply_raise()
print(emp_1.pay)


print(Employee.num_of_emps)