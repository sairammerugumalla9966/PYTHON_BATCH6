
# Polymorphism in OOPs Python  

# poly --> many , morphs ---> forms
# an ability to do more than one task.

# Operator overloading : an operator performing differnt operations in different cases. 

#  ' + '  --> Addition when input is integer 
#  ' + '  --> concatination 
 
print(10+20)   # addition 

print("Sai" + "Ram")  # concatination 

print([1,2,3] + [4,5,6,7,8])  # concatination 


# '*' ---> interger as input then multiplication 
# packing and unpacking arguments 
# repitation  

print(30*2)  # multiplication operator 
print("Sairam " * 3)  # repitation operator 


# polymorphism in functions ??
# if a function handles more than one datatype and different parameter sizes , then it is also called as polymorphism 

print(30)
print("sairam" + "Rocky")
print(20+40)
print(len("rocky"))


class A:
    def func(self):
        print("this is class A function")

class B:
    def func(self):
        print("this is class B function")

class C:
    def func(self):
        print("this is class C function")


def poly(obj):
    obj.func()

obj1 = A()
poly(obj1)

obj2 = B()
poly(obj2)


# method overridding : 



class Parent:
    def method(self):
        print("this is parent method")

class Child(Parent):
    def method1(self):
        print("this is child method")

    def method(self):
        print("this is child method")


c =Child()
c.method() 



# advance python 

# modules , packages , virtual environment 
# exception handling 
# decorators , generators , iterators 
# file handling 

# Database ---> sql , MYSQL , SQLITE

# Frameworks --> Flask , Django 

# Project  



