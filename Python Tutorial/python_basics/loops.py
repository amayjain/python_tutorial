# for loops --> used to iterate over a string, list, tuple, set, or dictionary

for i in range(6): # helpful to use range function to iterate --> range(start, stop, step)
    print(i)

monday_temperatures = [9.1, 8.8, 7.6]

for temperature in monday_temperatures:
    print(round(temperature))

for letter in "hello":
    print(letter.title())


#looping through a dictionary
student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}

for grades in student_grades.items(): # returns a tuple of (key, value)
    print(grades)

for grades in student_grades.keys():
    print(grades)

for grades in student_grades.values():
    print(grades)


# while loops --> runs while condition is True

a = 3

while a > 0:
    print(1)
    a -= 1


user = ""

while user != "pypy":
    user = input("enter username: ")

# use break and continue
# break --> exits out of loop
# continue --> stops current iteration and moves onto next iteration

while True:
    user = input("enter username: ")
    if user == "pypy":
        break
    else:
        continue
