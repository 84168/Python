# Polymorphism: Operator Overloading
# When the same operator is allowed to have different meaning according to the context.
# Operators & Dunder functions

# a + b        a._add__(b)
# a - b        a._sub__(b)
# a * b        a__mul___(b)
# a / b        a__ truediv___(b)
# a % b        a__mod___(b)



class complex:
    def __init__(self,real,img):
        self.real=real
        self.img = img
    
    def showNum(self):
        print(self.real, "i" , self.img, "j")

    # def add(self,num2):
    #     newReal = self.real +num2.real
    #     newImg = self.img + num2.img
    #     return complex(newReal, newImg)

    # DUNDER FUNCTION 
#     def __add__(self,num2):
#         newReal = self.real +num2.real
#         newImg = self.img + num2.img
#         return complex(newReal, newImg)

#     def __sub__(self,num2):
#         newReal = self.real - num2.real
#         newImg = self.real - num2.real

#         return complex(newReal, newImg)
    
# num1 = complex(1,3) 
# num2 = complex(4,6)

# num1.showNum()
# num2.showNum()

# # without dunder function
# # num3 = num1.add(num2)
# # num3.showNum()

# # with dunder function
# num3 = num1 + num2
# num3.showNum()

# num3 = num1 - num2
# num3.showNum()

# EXAMPLE
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
    
#     def area(self):
#         print("area is " , 3.14 * self.radius ** 2) 

#     def perimeter(self):
#         print("perimeter is ", 2 * 3.14 * self.radius)

# c1 = Circle(21)
# c1.area()
# c1.perimeter()
# print("radius is" , c1.radius)


# EXAMPLE
# class Employee:
#     def __init__(self, role, department, salary):
#         self.role = role
#         self.department = department
#         self.salary = salary
    
#     def showDetail(self):
#         print(self.role, self.department, self.salary)

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT dept", "20000") # for all the engineer these are fixed
#     def showDetail(self):
#         print(self.name, self.age)


# e1 = Employee("HR", "laszy deprtment", 2000)
# e1.showDetail()

# e1 = Engineer("tarun" ,"23")
# e1.showDetail()



# EXAMPLE 
class Order:
    def __init__(self, item,price):
        self.item = item
        self.price = price
    
    def __gt__(self, odr2):
        if(self.price > odr2.price):
            return True
        else :
            return False
        

odr1 = Order("Chips", 30)
odr2 = Order("tea", 15)

print(odr1 > odr2)

