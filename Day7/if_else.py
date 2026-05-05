# conditional statements in python 

# if , if-else --> 

'''
if condition:   # if true then excecute orelse move to next part 
    statements 
    block of code 
    block of code


'''
'''
a=10
if a>9:
    print("sairam")
    print("sairam")
    print("sairam")
    print("sairam")
    print("sairam")
    print("sairam")

else:
    print("out of if condition")


num = 10
if num % 2 == 0:
    print("even")

else:
    print("odd")


age = int(input("enter your age : "))

if age >= 60:
    print("senior citizen")

elif age <= 18:
    print("minor")

else: 
    print("major")
    



# grading system 

# marks > = 90 ---> outstanding 
# marks > = 80 ---> A grade 
# marks > = 70 ---> B grade 
# marks > = 60 ---> C grade
# marks > = 50 ---> D grade
# # marks < 50 ---> Fail  





marks = int(input("enter your marks : "))

if marks >= 90:
    print("outstanding ")

elif marks >= 80:
    print("A grade")

elif marks >= 70:
    print("B grade")

elif marks >= 60:
    print("C grade")

elif marks >= 50:
    print("D grade")

else:
    print("Fail")



# login system 
username = "Rocky" 
password = "Ex143"

if username == "Rocky" and password == "No Ex":
    print("login succeseful")

else:
    print("login failed")


# role based access 

role =input("enter your role : ")

if role == "admin":
    print("full access")

elif role == "employee":
    print("partial access")

else:
    print("no access")



# nested if : if inside a if 

#if condition :
    #if condition :
        # block of code 
        # block of code 

#else :
    # block of code 


user_name =input("enter your username : ")

if user_name == "Rocky9966":
    password  =input("enter your password : ")
    if password == "RockyBhai":
        print("login success")
    else :
        print("wrong password")

else:
    print("user not found")
'''
# check balance 

balance = 50000
amount = 0
if amount <= balance:
    if amount > 0 :
        print("withdraw successful")
    else: 
        print("invalid amount")

else: 
    print("insufficent balance")








