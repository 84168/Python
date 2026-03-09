# To map with real world scenarios, we started using objects in code.
# This is called object oriented programming.
# USING FUNCTIONS REDUNDENCY DECREASES AND REUSABILITY INCREASES

# CLASS IS A BLUEPRINT OF OBJECTS
# class Student:
#     Name = "Taurn Parmar"

# s1 = Student() # CREATING INSTANCES OF CLASS or object
# print(s1)
# print(type(s1))
# print(s1.Name) # case sensitive s1.name shows error



#   All classes have a function called _init_O, which is always executed when the object is being initiated.
# class Student:
#     # DEFAULT CONSTRUCTOR
#     def __init__(self):
#         pass

#     college_name = "ABC"                                        # is a class attribute common to all objects
#     # PARAMETRIZED CONSTRUCTOR
#     def __init__(self, fullname,marks):                         # CONSTRUCTOR WITH DEFAULT METHOD INIT SELF IS POINTING TO THE OBJECT
#         self.name = fullname                                    # unique to all objects || object attribute
#         self.marks = marks
#         print(self)

#     def avg(self):
#         sum =0 
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "your avg marks is " , round(sum / 3, 2))

    
#     def hello(self):                                            # METHODS ARE FUNCTIONS THAT BELONG TO OBJECTS...
#         print("hello ", self.name, "your marks are ", self.marks)

# s1 = Student("Rahul",[23,34,56])
# s1.avg()




# STATIC METHODS that dont use the self parameter (work at class level)
# class student :


#     @staticmethod               # a DECORATOR : changing the behavior of normal function
#     def college():
#         print("college")

# s1 = student()
# s1.college()

# ABSTRACTION : hiding the implementation detail of a class and only showing the essential features to the user
# class car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False
    
#     def start(self):
#         self.clutch = True  #INTERNAL DETAIL HDDEN FROM USER
#         self.acc = True
#         print("car started...")
    
# car1 = car()
# car1.start()

# ENCAPSULATION: wraping data and function into a sngle unit (object)

class Account:
    def __init__ (self,bal,acc):
        self.bal = bal
        self.acc = acc
    
    def get_bal(self):
        print(self.bal)
    
    def debit(self, amount):
        self.bal = self.bal - amount
        print(amount,"is debited from your account","current balance is ", self.bal)

    def credit(self, amount):
        self.bal = self.bal + amount
        print(amount ,"is credited to you account","current balance is",self.bal)

user1 = Account(4000,100)
user1.get_bal()
user1.debit(2000)
user1.credit(100)

user1 = Account(400,101)
user1.get_bal()
user1.debit(200)
user1.credit(100)

