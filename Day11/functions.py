# Functions in python 

# what is a function ??
# function is reuseable block of code 
# write once use multiple times 

# organise code 
# for reuseability 
# makes the code in a structured way

# synatx :

# def functionName():  # function definition 
    # block of code
    # # block of code 
    # # block of code 
    # # block of code 
    # # block of code 
    # # block of code 
    # # block of code 
    #pass
#functionName()  # function calling 
 
#def function_name():
    # block of code  
    # pass
# function_name()


# Naming convention : camelCase naming convention , snake_case naming convention  
# snake_case 
# camelCase


def sample_func():
    print("function called successfully")

sample_func()


# function without parameters 
def addition():
    a=50
    b=30
    c=a+b
    print(c)
    return c

#print(addition())

add = addition()
print(add , "from the variable")


# Parameters --> variables which are defined inside a function 
# Arguments ---> values given to the parameters while function calling 

# why ?? for dynamic programming 

# function with parameters 

def add_func(a,b,c):
    res=a+b+c
    return res

#print(addition())

print(add_func(20,50,40))
print(add_func(27,56,47))
print(add_func(77,66,97))

# if you are not passing same number of arguments 
# which are declared as parameters in a function , then you'll get an error 


