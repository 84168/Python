# DEl keyword
# class student:
#     def __init__(self,name):
#         self.name = name

# s1 = student("karan")
# print(s1.name)
# del s1.name

# print(s1.name)

#  PRIVATE attributes and methods Private attributes & methods are meant 
# to be used only within the class and are not accessible from outside the class.

# class Account:
#     def __init__(self,acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass              # __acc_pass two underscore means it is private 

#     def printPass(self):
#         print("Password is :",self.__acc_pass)      # PRIVATE  accessed inside the class

# acc1 = Account("12345", "abcde")

# print(acc1.acc_no)
# #print(acc1.__acc_pass)              # shows Error cause the __acc_pass is private and cannot be accessed out of the class

# acc1.printPass()


# INHERITANCE : When one class(child/derived) derives the properties & methods of another class(parent/base).
# SINGLE , MULTILEVEL , MULTIPLE INHERIANCE

# class car: 
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("car stopped")
    

# class toyota(car):          # INHERIT FROM CAR SINGLE INHERTANCE
#     def __init__(self,name):
#         self.name = name


# class fortuner(toyota):             # MULTILEVEL INHERITANCE
#     def __init__(self,type):
#         self.type = type
    

# car1 = toyota("fortuner")
# car2 = toyota("prius")
# car3 = fortuner("electric")

# print(car1.name)
# print(car1.start())

# print(car3.type)
# #print(car3.name)
# print(car3.start())
# print(car3.stop())


# class Car:
#     def __init__(self,type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car Started...")
    
#     @staticmethod
#     def stop():
#         print("car stopped...")
    
# class toyota(Car):
#     def __init__(self,name,type):
#         super().__init__(type)
#         self.name = name
#         super().start()

# car1 = toyota("patisu", "electric")
# print(car1.type)
# print(car1.start())


# STATIC METHOD CANT ACCESS OR MODIFY CLASS STATER AND GENERALLY FRO UTILITY
# class Person:
#     name = "anonymous"
#     # def changeName(self, name):
#     #     # Person.name = name # or
#     #     self.__class__.name = name

#     @classmethod
#     def changeName(cls, name):
#         cls.name = name
    
# p1 = Person()
# p1.changeName("rahul bhai")
# print(p1.name)
# print(Person.name)



# class Student:
#     def __init__(self,phy,che,math):
#         self.phy = phy
#         self.che = che
#         self.math = math
#         # self.percentage = str((self.phy + self.che+self.math) / 3) # afer some time if we change hte marks but now percentage cant be chaanged 
#                                                                     # we can create a method to change the percentage
        
#     def cal_per(self):
#         self.percentage = str((self.phy + self.che+self.math) / 3)



# stu1 = Student(90,90,90)
# # print(stu1.percentage)
# stu1.phy = 0

# stu1.cal_per()
# print(stu1.percentage)


# PROPERTY  we use @PROPPERTY decorator on any method in the class to use the method as a property
class Student:
    def __init__(self,phy, che, math):
        self.phy = phy
        self.che = che
        self.math = math
    
    @property
    def percentage(self):
        return str((self.phy+self.che+self.math) / 3) + "%" 
    
stu1 = Student(98, 97, 99)
print(stu1.percentage)
stu1.che = 86
print(stu1.percentage)


