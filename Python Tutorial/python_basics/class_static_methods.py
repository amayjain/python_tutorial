class Employee:

    num_of_emps = 0
    raise_amount = 1.04 

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_of_emps += 1 

    
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) 

    @classmethod # decorator that makes method take in 'class' as argument instead of 'self' --> use "cls" as argument
    def set_raise_amt(cls, amount): # using a class method to change variable of whole class and instances
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str): #creates a new instance given a string with all the information separated by dashes
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)
    
    @staticmethod #don't need "self" or "cls" as first argument
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6: # 5 is saturday and 6 is sunday, 0 is monday
            return False
        return True





emp_1 = Employee("Amay", "Jain", 50000)
emp_2 = Employee("Test", "User", 60000)


Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)


emp_str_1 = "Amay-Jain-49000"
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.email)


import datetime
my_date = datetime.date(2020, 12, 31)

print(Employee.is_workday(my_date)) #calling upon a static method using class_name.static_method(argument)