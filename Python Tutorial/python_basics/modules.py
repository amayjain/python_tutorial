import time
import os
import pandas 

while True:
    if os.path.exists("txt_files/vegetables.txt")
        with open("txt_files/vegetables.txt") as file:
            print(file.read())
    else:
        print("File does not exist.")
    time.sleep(10)




while True:
    if os.path.exists("txt_files/temps_today.csv"):
        data = pandas.read_csv("txt_files/temps_today.csv") #creates a dataframe object
        print(data.mean()["st1"])
    else:
        print("File does not exist.")
    time.sleep(10)