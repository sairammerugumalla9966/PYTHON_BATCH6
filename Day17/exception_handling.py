# EXCEPTION HANDLING IN PYTHON 

# Exception ?? handling runtime error 

# runtime error ?? 

# Error ???   ---> problem in a program ,prevents the program from running properly 

# types of errors --> syntax error , logical errors 

def add(a,b):
    return a-b

print(add(30,10))

print("sairam")

# Runtime errors( Exceptions ) ?? errors caused by the users 

# exception handling blocks 

# try block ----> risky code 
# except block ---> handles exception  
# else block --> runs if no exception 
# finally ---> always executes 

try:
    print(10/0)

except ZeroDivisionError as zde:
    print(zde)


print("exception handled")

try:

    a = float(input("enter a value "))
    b = float(input("enter b value "))

    res = a/b
    print(res)

except ZeroDivisionError as z:
    print(z)

except Exception as e:
    print("invalid input please enter numeric value ",e)

else:
    print("all is well")

finally:
    print("the end")


class AgeError(Exception):
    pass

try :
    age = int(input("enter your age : "))
    if age < 18:
        raise AgeError("age must be 18 years,please get back again ")

except AgeError as a:
    print(a)






