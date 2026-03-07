str = "heismy\nthis is in next line "
print(str[5:len(str)])
print(str[-4:-1])
print(str.endswith("line "))
print(str.capitalize())
print(str.replace("next" , "X"))
print(str.find("this")) # STARTING INDEX OF 'THIS' first time jaha tha
print(str.find("z"))
# str = input('enter name :')
# print(len(str))
# print(str.count("$"))

marks = int(input("enter marks:"))
if(marks >= 90):
    print("A")
elif(marks < 90 and marks >=80):
    print("B")
elif(marks < 80 and marks >=70):
    print("C")
elif(marks < 70):
    print("D")  