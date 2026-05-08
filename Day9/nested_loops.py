# nested loops : loop inside a loop 


# for each and every i value , j will excecute all the times  

for i in range(1,4):  # 1,2,3 
    for j in range(1,4): # 1,2,3 
        print(i,j)

# 1,1 
# 1,2
# 1,3
# 2,1
# 2,2 
# 2,3
# 3,1
# 3,2
# 3,3


# # # # # 
# # # # #
# # # # #
# # # # #

for i in range(1,5): 
    for j in range(1,10):
        print("#", end =" ")
    print() # next line 

 # end = " "  ---> it makes the cursor stay on the same line 


name = input("enter any character : ")
if name in "aeiou":
    print("vowel")
else:
    print("consonant")
