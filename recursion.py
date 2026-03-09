# FUNCTION CALLING FUNCTION 
def show(n):
    if(n == 0) :
        return
    print(n, end=" ")
    show(n-1)


def fact(a):
    if(a == 1 ):
        return 1
    
    fat = a * fact(a-1)
    return fat

sum = 0
def nSum(n):
    if(n == 0):
        return 0
    sum = n + nSum(n-1)
    return sum

list = [1,2,3,4,5,6]
def printlist(list, idx=0):
    if(idx >= len(list)):
        return 
    
    print(list[idx], end=" ")
    printlist(list, idx = idx+1)

printlist(list)