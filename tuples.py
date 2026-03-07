# STRINGS ARE IMMUTABLE AND LISTS ARE MUTABLE
list =[1.0,2,4,6,4]
print(type(list[1]))
print(len(list))
list[0] = 5
print(list)

#SLICING IN LIST
print(list[1:4])
print(list[3:])
print(list[:len(list)])
print(list[-3:-1])

# METHODS IN LIST
list.append(9) 
list.sort() # ascending 
list.sort(reverse=True) # descending
list.reverse() # in reverse order done in original list
list.insert(0 , 100) # insert(idx, elemet) do not replace
list.remove(4) # remove(element) remove first occurance of element
list.pop(0) # pop(idx) remove ele at idx
print(list)

# TUPLES ARE IMMUTABLE
tup = (1,2,3,"tarun")
print(type(tup))
print(tup[1])
print(tup)

# SINGLE ELEMENT TUPLE
tup1 = (1) 
print(type(tup1)) # it is integer

tup1 = (1.0)
print(type(tup1)) # it is float

tup1 = ("hello")
print(type(tup1)) # it is string

tup1 = (1,)
print(type(tup)) # it is tuple

# TUPLES METHOD 
tup = (2,1,3,1)
print(tup.index(3)) # index(ele) return indx of first occurance of ele
print(tup.count(1)) # return count of ele

# EXAMPLE 1:
list =[]
mov = input("enter movie: ")
list.append(mov)
mov = input("enter movei: ")
list.append(mov)
mov = input("enter movie: ")
list.append(mov)
print(list)

# EXAMPLE 2:
list1 = [1,2,3,2,1]
list2 = list1.copy()
list2.reverse()
print("list 2 is : ",list2)

if(list1 == list2 ):
    print("true")
else:
    print("false")

# EXAMPLE 3:
tup = ("C","D","A","A","B","B","A")
print(tup.count("A"))

list =["C","D","A","A","B","B","A"]
list.sort()
print(list)


