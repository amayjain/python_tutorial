# open() used to open a file for reading
# .read() method stores file as a string
myfile = open("fruits.txt")
content = myfile.read()
myfile.close() # removes it from RAM


# closes file once block ends
with open("fruits.txt") as myfile:
    content1 = myfile.read()

print(content1)




# if file is somewhere else, you need to indicate filepath
with open("txt_files/fruits.txt", "r") as myfile:
    content2 = myfile.read()

print(content2)




# create a new file to write if it does not exist
with open("txt_files/vegetables.txt", "w") as myfile:
    content3 = myfile.write("Tomato\nCucumber\nOnion\n")
    myfile.write("Garlic")






#appending text to exisiting file
with open("txt_files/fruits.txt", "a+") as myfile: # "a+" is to be able to append and read 
    myfile.write("Okra\n")
    myfile.seek(0)   #put cursor back on first line
    content4 = myfile.read()

print(content4)


