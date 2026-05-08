# 
# # 
# # # 
# # # #
# # # # #
# Right angled triangle 
for i in range(1,6): # rows  1,2,3,4,5
    for j in range(i): # elements 
        print("*" , end=" ")
    print()


# reverse Right angled triangle 

# # # # #
# # # # 
# # # 
# #
# 

for i in range(5,0,-1):
    for j in range(i):
        print("*", end =" ")
    print()

'''
* * * * * 
* * * * 
* * * 
* * 
* 
'''

# number pattern 
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end =" ")
    print()

'''
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
'''

'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

'''

for i in range(1,6):
    for j in range(1,i+1):
        print(j , end=" ")
    print()


for i in range(1,6):
    for j in range(1,i+1):
        print(i , end=" ")
    print()


matrix =[[1,2,3],[4,5,6],[7,8,9],[99,88,77]]

for row in matrix:
    for value in row:
        print(value , end=" ")
    print()
    
'''
1 2 3
4 5 6 
7 8 9
99 88 77
'''
