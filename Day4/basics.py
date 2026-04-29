# key words : key words are reserved words in python that have some special meaning 

# if ,else ,for ,while , return , pass , def , True , False , break , continue , import , None

# should not declare them as variable names , function names , class names 
# they are case sensitive 
'''
import keyword
print(keyword.kwlist)   #---> display output


['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 
'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 
'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

'''

# Identifiers : are names given to variables , functions , classes 

a = 100

# rules for identifiers 

# it must start with letters(a-z , A-Z) or underscore ( _ )
# should not start with digits(0-9)
# should not start with special characters 
# can not start with keywords
# case-sensitive 

_value = 100
print(_value)

value = 90
print(value)

Value = 10
print(Value)

# Value != value

#~value = 100
#print(~value)

# for = "sairam"

# variables ---> variables are names which point to that particular memory location  
a = 99
print(a) # 99

a = "sairam"
print(a) # sairam

# dynamically typed ---> no need to declare any datatypes 

name = names = Name = "Rocky"
print(name)
print(Name)
print(names)

# multiple variables , multiple values 
x,y = 123.45, 1976.89
print(x)
print(y)


p = 787
p = "Rocky"
print(p)

total = 100+89+99+67
print(total)


print(a)


# input and output 

# input() --> used to give input from the user 

age = input("enter your age : ") #takes it as string
print(type(age))

# output  ---> used to display the output 

print("kjdhklhafkgkj")
print(age)



