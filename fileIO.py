# can be used to perform operatoin on a file 
# OPEN READ AND CLOSE FILE (we have to open file before reading and writing)
# 'r'     open for reading (default)
# 'w'     open for writing, truncating the file first
# 'x'     create a new file and open it for writing
# 'a'     open for writing, appending to the end of the file if it exists
# 'b'     binary mode
# 't'     text mode (default)
# '+'     open a disk file for updating (reading and writing)


import os
# f = open('file.txt', 'r') # open(fileName, Mode/r/w) default it is read
                          # if file not present then full path should be passed
# data = f.read()
# data = f.read(5) # only 5 characters
# data = f.readline() # read only single line, empty line is printed if not line in file
# print(data)
# print(type(data))
# f.close()

# f = open("file.txt", "w")
# f.write("this is the next updated line") # PREVIOUS DATA IN FILE IS REMOVED AND THIS IS STORED
# f.close()

# f = open("file.txt", "a")
# f.write("\n this is appended line") # appended to next line in file
# f.close()

# f = open("file.txt" , "r+") # pointer starts from file starting no truncate
# f.write("this is i worte using R+ which is used for read and write operation")
# print(f.read())
# f.close()

# f = open("file.txt" , "w+") # file opened in truncated mode
# f.write("this is i worte using R+ which is used for read and write operation")
# # Move the cursor back to the beginning (index 0)
# f.seek(0)
# print(f.read())
# f.close()

# f = open("file.txt","a+") # a+ is used for the append and read and the cursor strt at the end of data no truncate
# f.read()
# f.write("\n we used a+")
# f.seek(0)
# print(f.read())
# f.close()

# with open("file.txt", "r") as f:  # WITH AUTOMATICALLY CLOSES THE FILE
#    print(f.read())
#    os.remove("file.txt")

# with open("file.txt" , "a+") as f:
#     f.write("Hi everyone")
#     f.write("\nwe are learning file I/O \nusing JAvA. \ni like programmin in java")

#     with open("file.txt","r") as f1:
#         print(f1.read())

# with open("file.txt","r+") as f :
#     data = f.read()
#     print(type(data))

# new_data = data.replace("Java", "Python")
# with open("file.txt", "w") as f:
#     f.write(new_data)


# with open("file.txt", "r") as f:
#     data = f.read()

# print(data)
# if(data.find("Leaning") !=-1): # here .find do not return TRUE or FALSE it returns integer it returns -1 if not found
#     print("True")
# else:
#     print("false")

# word = "learning"
# data = True
# line_no = 0
# with open("file.txt", "r")as f:
#     while data :
#         data = f.readline()
#         if(word in data):
#             print(line_no)
#         line_no += 1

# with open("file.txt" ,"w") as f:
#     f.write("1,2,3,4,5,6,7")

# count_even = 0
# list = []
# with open("file.txt","r") as f:
#     data = f.read()

# num =""
# for i in range(len(data)):
#     if(data[i] == ","):
#         new_num = int(num)
#         list.append(int(new_num))
#         num = ""
#     else :
#         num += data[i]

# for item in list :
#     if(item % 2 == 0):
#         print(item)

count = 0 
with open("file.txt" , "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums : 
        if(int(val) % 2. == 0):
            # print(val)
            count += 1

print(count)