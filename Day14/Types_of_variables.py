'''
# Types of variables in OOPs python :

# local variables : Variables which are declared inside a method (function)
# static or class variables  : variables which are declared outside a method and inside a class 

class A:
    s_var1=100
    s_var2=200

    def Sample(self):
        print("sample method")


# if you want to access class variables within class methods , then sefl.variablename or Classname.variablename
    def method1(self):
        print("accessed through classmethod",self.s_var1)     
        print("accessed through classmethod",self.s_var2)
        print("accessed through classmethod",self.s_var)
        print("accessed through classmethod",A.s_var)

    s_var=300


class B:
    s_var4=400
    def demo(self):
        print("demo method")

print(B.s_var4)
# print(B.s_var) ---> AttributeError: type object 'B' has no attribute 's_var'. Did you mean: 's_var4'?


# access class variables through class name 
print(A.s_var1 , A.s_var2)
print(A.s_var2)
print(A.s_var)


#class variables can be created , updated , accessed , deleted using classname  

A.s_var = 9999
print("updated class variable : ",A.s_var)

# access class variables through object 
obj = A()
obj.s_var1 = 7777
obj.method1()
print(obj.s_var)
print("updated through class oject : ",obj.s_var1)
print(obj.s_var2)

obj1=A()
print(obj1.s_var1)
print(obj1.s_var)

'''
# Instance variables : whenever a variable is created for an object 

# 2 ways to access instance variables 

# self.variablename = variablename 
# object.variablename = value 


class A:

    def __init__(self,a,b,c):
        self.instancevar1 = a 
        self.instancevar2 = b 
        self.instancevar3 = c

    def updatevariable(self,newvalue):
        self.instancevar1 = newvalue

obj=A(10,20,30)
print("instance variable accessed through object : ",obj.instancevar1)
print("instance variable accessed through object : ",obj.instancevar2)

#obj.instancevar3 = 30
obj.instancevar4 = 40

print(obj.instancevar3)

obj.updatevariable(4000)
print("updated instancevariable : ",obj.instancevar1)

obj1=A(100,200,300)
print(obj1.instancevar1)
print(obj1.instancevar2)
print(obj1.instancevar3) 

# print(obj1.instancevar4) # AttributeError: 'A' object has no attribute 'instancevar4'. Did you mean: 'instancevar1'?









