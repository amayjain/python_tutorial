def area(a, b):     # can also have default arguments such as def area(a = 4, b = 6)
    return a * b

print(area(4, 5)) # positional arguments
print(area(a = 4, b = 5)) # keyword arguments
print(area(b = 4, a = 5)) # also works




# *args - arbitrary number of arguments
def mean(*args): 
    return args   # returns a tuple of all arguments you passed


def mean1(*args):
    return sum(args) / len(args)

print(mean1(1, 2, 4))







# **kwargs --> keyword arguments
def mean2(**kwargs):
    return kwargs    # returns a dictionary


def mean3(**kwargs):
    return sum(kwargs.values()) / len(kwargs.values())

print(mean3(a = 1, b = 2, c = 3))

    






