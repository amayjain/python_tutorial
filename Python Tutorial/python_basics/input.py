def weather_condition(temperature):
    if temperature > 7:
        return "warm"
    else:
        return "cold"

print(weather_condition(5))

#input() gets input from user and produces a string
user_input = float(input("Enter temperature:")) #convert to float, so you can compare in weather_condition() function 

print(weather_condition(user_input))



#String formatting

user_input1 = input("Enter your name: ")
message = "Hello %s!" % user_input1 # % user_input1 will replace %s
message2 = f"Hello {user_input1}"
print(message)


name = input("Enter your name: ")
surname = input("Enter your surname: ")
message3 = "Hello %s %s" % (name, surname)
message4 = f"Hello {name} {surname}"
print(message3)