# count = 1
# while(count <= 5):
#     print("hello", count)
#     count += 1

list = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# idx = 0
# while(idx < len(list) ):
#     print(list[idx])
#     idx += 1

# for val in list:
#     print(val)
# else:              # THIS ELSE WILL RUN AFTER COMPLETING EACH ITERATION OF LOOP IF BREAK THEN ELSE NOT EXECUTED
#     print("end")

# range(ele) => from 0 to ele - 1
# seq = range(10)
# for i in seq :
#     print(i)

# seq = range(1,5) # range(start, end)
# for i in seq:
#     print(i)

# seq = range(1,5,2) # range(start, end, stepsize (can be negative) )
# for i in seq:
#     print(i)

# num = int(input("ente number: "))
# for i in range(1,11,2):
#     print(i * num)

# for i in range(5):
#     pass # IF DONT WANT TO DO ANYTHING IN LOOP

# print("some usefull work")

# i = 1
# sum =0
# n = int(input("enter valu if N :"))
# while(i<=n):
#     sum += i
#     i += 1
# print(sum)

# FACTORIAL 
n = int(input("enter num"))
fact = 1
while(n>0):
    fact *= n
    n -= 1
print(fact)