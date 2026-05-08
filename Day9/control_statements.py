'''
# Loop control statements : 

# break statement : is used to terminate the loop 

for attempt in range(1,4):
    pin = input("enter your pin : ")

    if pin =="Rocky":
        print("login successful")
        break

    print("wrong pin ,please try again")

'''

products =["mobile","mouse","pen","laptop","pizza","keyboard","desktop"]

for i in products:

    if i == "topless":
        print("product found")
        print("Abbaaaa Saaai Raaaammm... ")
        break

    print("searching :" ,i)

print("Jampar mai bamper...")



# continue  : skips the current iteration and moves to next itertaion 

for i in range(1,6):
    if i == 3:
        continue
    print(i)


users = ["Admin","Sairam","sreenadh","Blocked","Rocky","powerstar","chiru"]

for user in users:
    if user == "Blocked":
        continue
    
    print("welcome",user)


# Pass : it is a placeholder  

class Money:
    def sample(self):
        pass

for i in range(1,5):
    pass

class PassClass:
    pass



