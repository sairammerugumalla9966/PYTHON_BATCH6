
# OOPS in python 

# paradigms  ???  approach / style 

# procedural approach/ paradigm ---> step by step (c,c++)
# functional paradigm ---> pure functions 
# object oriented paradigm ---> create objects and solve the problem 


# OOPS concepts ---> class , object , constructor , ineritance , polymorphism , encapsulation , abstraction 

# oops --> object oriented programming system 

# class : it is a blueprint / template used to create objects 
# object : byproduct of a class or instance of a class 

# from one class you can create unlimited objects 

# eg : pen is a object 

# properties : name , color , brand , price , model 
# behaviour : it is used to write something 

# eg : you are an object 
 
# properties : name ,color, professsion , age , height , weight , gender , DOB 
# behaviour : your own behaviour 

# in same way , In OOPs 
# properties ---> attiributes / variables 
# behaviour ---> methods / procedures / functions

# if you want to create objects in OOPs , we need to declare or define the class

# in python everything is an object and that objects comes from a class 

print(type(10))   # 10 is interger object 
print(type(10.77)) 
print(type(True)) 


# why OOPS ???

# extendabilty  
# data security 
# easy to handle real world complex problems
# buttom-up approach 
# modularity : parallel programming 
# one class can be used in another class 
# project development time will be redued 


'''
# class Syntax : combination of attributes and methods 

class ClassName:    # definition 
    # statements 
    # statements 
    # statements 
    # statements 

# PascalCase naming conventions 



class SampleClass:
    a=10
    b=20

print(SampleClass.a)
print(SampleClass.b)

# how to create objects ? 

class SampleClass:
    a=200
    b=20

obj = SampleClass()   # object creation
print(obj.a , obj.b)
print(obj.b)


obj1 = SampleClass() 
obj1.a = 100
print("from obj1 : ",obj1.a)


obj2 = SampleClass() 
print("from obj2: ",obj2.a)


'''

class SampleClass:
    a=100
    b=200
    def samplemethod(self):
        print("this is a method from this class")

obj = SampleClass()
print(obj.a)
print(obj.b)
obj.samplemethod()













































