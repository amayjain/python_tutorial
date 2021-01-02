#newlist = [*expression* for item in iterable if condition == True]

temps = [221, 234, 340, 230]

new_temps = [temp / 10 for temp in temps] #new way using list comprehension

''' new_temps = []
for temp in temps:
    new_temps.append(temp / 10)''' #old way using a for loop

print(new_temps)





temps1 = [221, 234, 340, -9999, 230]
new_temps1 = [temp / 10 for temp in temps1 if temp != -9999]
print(new_temps1)





#if / else list comprehension where if/else goes in between expression and "for" statement
temps2 = list(temps1)
new_temps2 = [temp / 10 if temp != -9999 else 0 for temp in temps2] # -9999 is replaced by 0
print(new_temps2)
