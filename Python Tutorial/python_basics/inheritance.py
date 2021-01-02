class Employee:

    raise_amount = 1.04 
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
    
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) 


# "Developer" class inheriting all attributes and methods of "Employee" class (the parent class)
# overwrites parent class for an instance of a subclass
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) # let parent(Employee) class handle first three attributes
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay) 
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp) 
    
    def print_emp(self):
        for emp in self.employees:
            print("-->", emp.fullname())
    

dev_1 = Developer("Amay", "Jain", 50000, "Python")
dev_2 = Developer("Test", "User", 60000, "C++")

mgr_1 = Manager("Sue", "Smith", 90000, [dev_1])

print(isinstance(mgr_1, Manager))
print(issubclass(Developer, Employee))

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.print_emp()

mgr_1.remove_emp(dev_1)
mgr_1.print_emp()

#print(help(Developer))

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)


print(dev_1.prog_lang)
print(dev_2.prog_lang)
