#functions treated as objects where they can be assigned to variables, passed as arguments, or returned

def square(x):
    return x * x

f = square # setting variable "f" equal to function
'''z = square()''' # don't set variable equal to square() because that calls upon the function and produces an error with no arguments

print(f)
print(f(5))





def cube(x):
    return x * x * x


def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)

cubes = my_map(cube, [i for i in range(1, 6)])
print(cubes)






def logger(msg):

    def log_message():
        print("Log:", msg)
    
    return log_message

log_hi = logger("Hi!") # stores the function log_message with "Hi!"
log_hi() # calls upon stored function
    