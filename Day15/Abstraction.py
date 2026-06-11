# Abstraction in OOPS python 
# means hiding implimentation details and showing only essential features 

# Car
# you know : start car , stop , accelerate , brake 
# what you dont know : engine combustion , fuel injection , piston moment 


# python provides abstraction through : abc module ---> abstract classes , abstract methods 

'''
class A:
    def method(self):
        pass

obj = A()
print(obj.method())

'''

from abc import ABC , abstractmethod

class Vechicle(ABC):

    @abstractmethod
    def start(self):
        pass
  
    def method(self):      # concrete methods 
        print("this is a normal method")

    @abstractmethod
    def stop(self):
        pass

class Child(Vechicle):
    def start(self):
        print(" start method is implemented through subclass")

    def method2(self):
        print("method2 is implemented")
    
    def stop(self):
        print("stop method is implemented through child class")

obj2= Child()
obj2.start()
obj2.method2()
obj2.stop()

# we can not directly create objects for abstract class but we can inherit abstract class and we can create objects 
# if abstract class is having abstract methods then the sub class should also have that methods 

# obj1=Vechicle()
# obj1.start()
# Vechicle.method()


# Abstract method : if a method is declared without implimentation logic , then it is called abstract method 

# abstract class : if a class contains one or more abstract methods ,then that class is called as abstract class 



