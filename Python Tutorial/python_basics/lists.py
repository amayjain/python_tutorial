monday_temperatures = [9.1, 8.8, 7.5]
monday_temperatures.append(8.1)
print(monday_temperatures)

monday_temperatures.clear()

monday_temperatures = [9.1, 8.8, 7.5]
print(monday_temperatures.index(8.8))
#.index(value, index to start search from and forwards)
monday_temperatures.index(8.8, 2)

#len() --> len(monday_temperatures) --> 3

#slicing
#list[start:stop] --> stops at one index before
#ex. list[0:2] --> gives elements at index 0 and 1
monday_temperatures[0:3]
#list[:stop] --> everything before stop index
#list[start:] --> everything after start including start
monday_temperatures[0:]
monday_temperatures[:3]
#negative indices --> last element has index of -1
monday_temperatures[-1] #returns 7.5

mystring = 'hello'
mystring[1] #returns 'e'

#chain index
monday_temperatures = ['hello', 1, 2, 3]
monday_temperatures[0][2] # returns 'l' --> accesses 0 index of list first, then second index of 'hello'