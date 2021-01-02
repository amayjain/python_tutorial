# use "def" to create functions --> name of function --> arguments in ()
# use "return" to get back a value from function

def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean

print(mean([1, 4, 5]))

student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}

# use type() function to check what type an argument is
# == is a comparison operator --> checks to see both sides are equal
# = assigns a value
# if/else --> conditional that checks using operators (True or False)

def mean2(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value)
    else:
        the_mean = sum(value) / len(value)
    
    return the_mean

print(mean2(student_grades))

# can use "and", "or", or "not" operators in if/else
# "and" --> both conditions need to be true
# "or" --> at least one condition needs to be true
# "not" --> returns reverse of result --> ex. not(True) returns False


# isinstance(object, type) --> checks to see if object is of specified type and returns True or False

if isinstance(3, int):
    print("yay")
else:
    print("nay")


# use "elif" to add on to if/else
"""
   if (condition):
        print('a')
   elif (condition2):
        print('b')
   else:
       print('c')
"""








