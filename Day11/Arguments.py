# Types of arguments in python

# parameters --> variables given at function defintion 
# arguments ---> values given while calling the function 

# types 
# positional args : if the values are assigned according to the position of the parameters , then it is called positional arguments 

def psargs_func(d,b,c,a):
    return a,b,c,d

print(psargs_func(40,20,30,10))


# keyword args : values are assigned with the parameter names while calling the function 
# it doesn't depend on the order / position of arguments 

def function(b,a):
    return b,a

print(function(b=40,a=20))


# default args: values are given while declaring the function parameters.if we wont pass the arguments then we get default values 
# if arguments are passed then  updated values are taken 

def function1(a=40,b=20,c=60,d=80):
    return a,b,c,d

print(function1(56,79))


# variable length args or arbitary args 

def func(*abd): # output will be in the form of tuple 
    return abd

print(func(10, 2.7,"sairam","trainer",True,56,79))


def func1(**kwargs):   # output will be in the form of dictionary 
    return kwargs

print(func1(name="sairam",age=29,jobrole="Trainer",active=True,place="hyd"))

