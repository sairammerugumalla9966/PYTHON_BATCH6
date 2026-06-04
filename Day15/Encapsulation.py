
# Encapsulation : binding data and methods together in a single unit called as class. 
# and also protect the data form accessing 

# why ?? 
# code will be organised and clean 
# prevent the data from accidental deletion 

# bank account 
# withdraw 
# deposite 
# check balance 
# loan balance 

# Data hiding : by using Access specifiers or access modifiers to security for data ---> public , private , protected 

# Abstraction : hiding implementation details or logic and allows only to use 

# Access specifiers or access modifiers 

# public access modifier : anywhere in the class we can use 

# if a data is declared as public access sepecifer , can can access data in the class , by creating objects , 
# we can access from the subclass and subclass objects 

'''
class Parent:
    public_data = "Rocky"
    def public_method(self):
        print(self.public_data)


class Child(Parent):
    def method(self):
        print(self.public_data)

obj = Child()
print(obj.public_data)     # Rocky
obj.public_method()        # Rocky
obj.method()            # Rocky
print()  

obj1 = Parent()
print(obj1.public_data)
obj1.public_method()


# protected access sepecifier : if the data is declared as protected access specifier
#  then it can be accesed only by the class and derived class 


class Parent:
    _protecteddata = "Rocky"
    def protected_method(self):
        print(self._protecteddata)


class Child(Parent):
    def method(self):
        print(self._protecteddata)


class Child1(Child):
    def method1(self):
        print(self._protecteddata)

obj = Child()
print(obj._protecteddata)     # Rocky
obj.protected_method()        # Rocky
obj.method()            # Rocky
print()  

obj1 = Parent()
print(obj1._protecteddata)
obj1.protected_method()

obj2 = Child1()
print(obj2._protecteddata)   # AttributeError: 'Child1' object has no attribute '_protecteddata'
obj2.method1()


# private access specifiers : can only be accessed by the class it is decalred 
#  

class Parent:
    __privatedata = "Rocky"
    def protected_method(self):
        print(self.__privatedata)


class Child():
    def method(self):
        print(self.__privatedata)


obj1 = Parent()
Parent.__privatedata = "sairam"
# print(obj1.__privatedata)
obj1.protected_method()


'''

class Bank:

    def __init__(self):
        self.__balance = 10000

    def deposite(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        self.__balance -= amount

    def check_balance(self):
        return self.__balance
    
b = Bank()
# print(b.__balance)    # private attributes can not be access through object 
# but they can be accessesd through methods 

print(b.check_balance())

b.deposite(5000)

print(b.check_balance())

b.withdraw(2000)

print(b.check_balance())




    

    









