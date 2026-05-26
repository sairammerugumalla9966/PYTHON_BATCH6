# Higher Order Functions in Python 

# A func that takes another function as an argument 
# A func returns another function 

# In python Functions are first-class objects : 

# functions can be stored in variables 
# functions can be passed to other functions 
# functions can be returned from functions 

'''
def outer(msg):
    def inner():
        print(msg)
    return inner()

print(outer("nenu avaru ........ Devuduuuuu"))


def calci(func,a,b):
    return func(a,b)

def sum(a,b):
    print("function called successfully")
    return a+b

def difference(a,b):
    return a-b

def multiply(a,b):
    return a*b

def division(a,b):
    return a/b

operation = calci(difference,25,15)
print(operation)

'''
# In-built Higher order functions 
# map() : applies a function to each every element of  sequence 

l=[1,2,3,4,5,6,7,8,9,10]
def square(x):
    return x*x

result = list(map(square,l))
print(result)

# filter() : filter the elements based on condition 

l1=[1,2,3,4,5,6,7,8,9,10]
def even(x):
    return x%2==0

res = list(filter(even,l1))
print(res)


# reduce() : applies a function cumulatively 

from functools import reduce

l2=[1,2,3,4,5,6,7,8,9,10]
def sum(x,y):
    return x+y

res = reduce(sum,l2)
print(res)




























# Higher order functions 

