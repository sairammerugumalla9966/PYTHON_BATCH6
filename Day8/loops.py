# Loops in python 

# what is a loop ??
# loops are used to excecute a block of code repeatedly until the condition is satisfied 

# sequence -- string , list , tuple , range()

# why ? 
# avoid duplicate code 
# process collections (list , string)
# automate tasks 

# for loop  ---> when you know how many times you have to iterate 
# while loop ---> when you  dont know how many times you have to iterate 

# syntax :
#for variable in sequence :
    # block of code 
    # block of code 
    # block of code 
    # block of code 


for i in range(1,11):   # n ---> n-1
    print("Rocky")


# range() --> (start , stop , step)
# start --- > where to start  # default --> 0
# stop ---> until which value # default --> n-1
# step --> gap between the iteration # default --> 1

for i in range(5):  # 0 , 1 , 2, 3 ,4 
    print(i)

for i in range(1,5):  # 1 , 2, 3 ,4 
    print(i)

for i in range(1,10,2):  # 1,3,5,7,9
    print(i)

for i in range(2,11,2):  # 1,3,5,7,9
    print(i)

name = "nidra pothe gaddidha"
for i in  name:
    print(i)


l = ["sairam" , 50000 ,"trainer" , 99.9 , True]
for i in l:
    print(i)



#  2 * 1 = 2
#  2 * 2 = 4
#  2 * 2 = 4

n = 2  
for i in range(1,11):
    print(n , " X " ,i ,"=" , n*i)




# while loop : while loops excecutes as long as condition is True. 

# syntax : 

# while condition :
    # statemets 
    # block of code 


# prime number ??
# ift should only be divisiable by 1 and itself 

# 10 --> 1 , 2, 5, 10
# 5 ---> 1 , 5
# 9 -- > 1 ,9  # check from 2 ---> 9 (9-1 = 8)

'''
num = 13
count = 0
for i in range(1,num+1):
    if num % i == 0:
        count += 1 

if count == 2: 
    print(num ,"is prime number")

else :
    print(num , "is not a prime number")
        
'''
# 13 % 2 == 0 --> False 
# 13 % 3 == 0 --> False 
# 13 % 4 == 0 --> False 


# 13 % 12 == 0 --> False 


num = 12
i = 1  # initialisation 
count = 0 
while i <= num :  # condition
    if num % i == 0:
        count += 1

    i+=1
# print(count)
if count == 2: 
    print(num ,"is prime number")

else :
    print(num , "is not a prime number")


# whike loop : write a program to find first 10 prime numbers 
# 2 , 3 , 5 , 7 , 11 , 13 , 17 , 19 , 23 , 29 
num = 2
count = 0
while count < 10:
    i=1
    factor = 0
    while i <= num:
        if num % i == 0:
            factor += 1
        i+=1

    if factor == 2:
        print(num)
        count +=1

    num +=1










