class Employee:
    
    def __init__(self, first, last, pay): #a constructor for attributes
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
    
    
    def fullname(self):
        return "{} {}".format(self.first, self.last)





emp_1 = Employee("Amay", "Jain", 50000) #creating an instance/object of class/datatype Employee
emp_2 = Employee("Test", "User", 60000)

print(emp_1.email)
print(emp_2.fullname()) #calling a class method





#instance variables - only for specific instance
'''emp_1.first = "Amay"
emp_1.last = "Jain"
emp_1.email = "amayjainsd@gmail.com"
emp_1.pay = 50000

print(emp_1.email)'''