import datetime
mynew = datetime.datetime.now()
print(mynew)

mynum = 10
mytext = "Hello"

print(mynum, mytext)

x = 10
y = "10"
sum1 = x + x
sum2 = y + y

print(sum1,sum2)
print(type(y))

#Boolean --> assign either True or False
boolean = True

#list
#can have lists inside lists
student_grades = [9.1, 8.8, 7.5]
print(list(range(1,10,2)))
print(mytext.upper())


mysum = sum(student_grades)
length = len(student_grades)
mean = mysum / length
print(mean)

#dictionary --> key and value
#use .keys() and .values() --> return a list
student_grades2 = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}
sum2 = sum(student_grades2.values())
mean2 = sum2 / length
print(mean2)

#tuple --> immutable - cannot add or remove items
monday_temp = (1, 4, 5)

