class Employee:

    raise_amount = 1.04 
    
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property # able to call a method as an attribute, so no parantheses at the end like when calling a normal method
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last    
    
    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None


emp_1 = Employee("Amay", "Jain")


emp_1.fullname = "John Smith" # accessing setter fullname method like an attribute

print(emp_1.first)
print(emp_1.email) # accessing email method like an attribute
print(emp_1.fullname)

del emp_1.fullname # accessing deleter