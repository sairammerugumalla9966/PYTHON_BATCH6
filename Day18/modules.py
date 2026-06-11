# Modules in python 

# modules ?? it is a python file containing classes , methods and variables, that can be reused in any other programs 

# class ??? blueprint to create objects 
# attributes and methods 

# method ??? block of similar code which contains variables and core logic 

# advantages :
# reuse code 
# time save 
# organised code 
# easy debugging and maintaince 

# types of modules :
# built-in modules ---> provided by python
 
# math module : 

# from math import sqrt

import math 
# ceil() ---> rounds of numbers to nearest largest number 

print(math.ceil(22.9))  
print(math.fabs(-100)) # gives positive float values 

print(math.factorial(5)) 
print(math.sqrt(81)) # sqrt
print(math.floor(11.6)) # gives floor value 
print(abs(-100))   # gives positive integers 



# Random module 
import random

print(random.random())   # gives random values between 0 and 1 

print(random.randint(1000,9999))  # otp generation 

print(random.choice([1,2,3,4,5,6,7,8,9,10]))

print(random.sample([1,2,3,4,5,6,7,8,9,10],3))


# Datetime module 

import datetime

today = datetime.datetime.now()
print(today)

# name , id , job , salary
# sairam , 1002 , trainer , 500000
# sairam , 1002 , trainer , 500000
# sairam , 1002 , trainer , 500000
# sairam , 1002 , trainer , 500000
# sairam , 1002 , trainer , 500000
# sairam , 1002 , trainer , 500000
# sairam , 1002 , trainer , 500000


# user-defined modules ---> created by developers 

