# operators in python 

# operator ??  
# symbol used to perform operations(tasks) on variables or values 
# + --> will add 2 or more vaiables or values 

# types : 

# arithematic operations 
# + , - * ,/ (division) ,// (floor divison) ,% (modulus), **(power)

print(100/25) # 4.0 (Q) (float)
print(100%25) # 0 (R)

print(10/3) #3.33334 (Q)
print(10//3) #3 (Q)

# comparision operators (True or False)

# == , != , < ,> <= ,>= 
a=10 
b=20
print(a==b)
print(a<b)


# logical operators 

# and , or , not 

print("admin"== "admin" and "1234" =="12345") # False

print("admin"== "admin" or "1234" =="12345")  # True


# assignment operators 

# = ,+= ,-= ,*= ,/= ,//= ,%= , **=
i=5
i+=1 # i=i+1
print(i)

# identity operators
# is , is not

a=[1,2]
b=[1,2]

print(a==b) #  True
print(a is b) # False


a=[1,2]
b=a

print(a==b) #  True
print(a is b) # True


# membership operators 
# in , not in 

names = ["sairam", "shiva","uday","pavan","narsimha","srenath"]

print("sairam" in names) # True
print("disha patani"  in names) # False
print("disha patani"  not in names) # True


# Bitwise operators 
# & , | , ^ ,<< , >> 


print(10+20) # int


