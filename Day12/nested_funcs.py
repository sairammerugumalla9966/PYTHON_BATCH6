'''
# Nested functions : function inside function 

# syntax :

def outer():
    print("outer function before inner function")
    print()

    def inner():
        print("inner function")
        print()
    inner()

    print("outer func after inner function")

outer()

print("outer func outside the function")



def login(username , password):

    def check():
        if username == "Rocky143" and password=="superman123":
            return True

        return False

    if check():
        print("login successful")
    else:
        print("invalid details")

login("sairam" ,"superman123")
login("Rocky143" ,"superman123")


def login(username , password):

    def check():
        if username == "Rocky143" and password=="superman123":
            print("login sunccessful")
        else:
            print("invalid details")
    check()

#login("sairam" ,"superman123")
login("Rocky143" ,"superman123")

'''


# Recursion in python : A function which calls itself 

# structure of recursion 
    # base condition 
    # recursion logic 


def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n-1)

countdown(10)



# factorial  5! = 5*4*3*2*1

def factorial(num):
    if num == 0:
        return 1
    
    return num * factorial(num-1)

res=factorial(5)
print(res)
