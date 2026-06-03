"""
# Inheritance in python 

# Inheritance : The ability to use attributes and methods in a newly created class from already existing class 
# or creating a new class from already existing class 


class A:
    A_var=10
    def A_func(self):
        print("this is class A function")

class B(A):
    B_var=100
    def B_func(self):
        print("this is class B function")

class C(A):
    C_var=100
    def C_func(self):
        print("this is class B function")



# obj = A()
# print(obj.B_var)   # AttributeError: 'A' object has no attribute 'B_var'. Did you mean: 'A_var'?
# A.B_func()  AttributeError: type object 'A' has no attribute 'B_func'. Did you mean: 'A_func'?

obj1 = B()
print(obj1.A_var)
obj1.A_func()

print(obj1.B_var)
obj1.B_func()

# all the child classes can access all the methods and attributes of the parent class 
# but parent class can not access child class methods and attributes 


# Types of inheritance 
# Single inheritance 

class Parent:
    def method(self):
        print("this is parent class method")


class Child(Parent):
    def method1(self):
        print("this is child class method")


child =  Child()
child.method1()
child.method()

parent = Parent()
# parent.method1()  # AttributeError: 'Parent' object has no attribute 'method1'. Did you mean: 'method'?

# Multiple inheritance 

class Father:
    def method_F(self):
        print("this is Father class method")

class Mother:
    def method_M(self):
        print("this is Mother class method")

    def method_F(self):
        print("this is Mother class method")


class Child(Mother,Father):
    def method1(self):
        print("this is child class method")


# if both parent classes have same methods , then whichever class is mentioned first while creating child class 
# that parent class will be inherited 

child =  Child()
child.method_M()
child.method_F()
child.method1()



# multi level inheritance 

class GrandFather:
    def method_GF(self):
        print("this is GrandFather class method")

class Father(GrandFather):
    def method_F(self):
        print("this is Father class method")

    def method_GF(self):
        print("this is Father class method")

class Child(Father):
    def method1(self):
        print("this is child class method")


child =  Child()
child.method_GF()
child.method_F()
child.method1()

father = Father()
father.method_GF()
father.method_F()

grandfather = GrandFather()
grandfather.method_GF()
# grandfather.method_F()

"""
# hierarichal inheritance 

class Parent:
    def method_P(self):
        print("this is Parent class method")

class Child1(Parent):
    def method_P(self):
        print("this is Father class method")

    def method_C1(self):
        print("this is Father class method")

class Child2(Parent):
    def method_C2(self):
        print("this is child class method")


# Hybrib inheritance 



