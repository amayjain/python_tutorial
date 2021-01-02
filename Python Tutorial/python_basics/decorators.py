# closure --> inner function has access to free variables of outer function
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)
    return inner_function # returns function

hi_func = outer_function("Hi") # inner function stores "Hi" and hi_func stores inner_function
bye_func = outer_function("Bye") # inner function stores "Bye" and bye_func stores inner_function

hi_func() # call upon hi_func variable which has inner_function stored, so it is really calling the inner_function
bye_func()







# decorators --> function that takes another function as an argument and gives it functionality
def decorator_function(original_function):
    def wrapper_function():
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function


def display():
    print("display function ran")

decorated_display = decorator_function(display)

decorated_display()



#same as above but with decorator
def decorator_function1(original_function1):
    def wrapper_function1(*args, **kwargs): # need to make sure original_function1 can handle any number of arguments
        print("wrapper executed this before {}".format(original_function1.__name__))
        return original_function1(*args, **kwargs)
    return wrapper_function1

@decorator_function1 # same as display1 = decorator_function1(display1)
def display1():
    print("display function ran")


@decorator_function1
def display_info(name, age):
    print("display_info ran with arguments ({}, {})".format(name, age))




display1()
display_info("Amay", 18)