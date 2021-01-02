student_grades = {"Mary": 9.1, "Sim": 8.8, "John": 7.5}
#access value of key with dict[key]
student_grades["Sim"] #returns 8.8

#changing a dictionary's value at a key
eng_port = {"rain": "chuva", "sun": "sol"}
eng_port["sun"] = "mar"
print(eng_port)

#converting data types
data = (1, 2, 3)
list(data)
[1, 2, 3]

data = [1, 2, 3]
tuple(data)
(1, 2, 3) 

data = [["name", "John"], ["surname", "smith"]]
dict(data)
{'name': 'John', 'surname': 'smith'}
