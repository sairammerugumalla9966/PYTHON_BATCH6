'''
name = "chiru"
# print(dir(name))

"""
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum',
 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',  
'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex',
'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate',
'upper', 'zfill'

"""


# Indexing : means accessing individual characters using position(intergers)

# positive index   (0 to n-1)
# negative index  (-1 to end of the string)

name = "chiru jvasdjlndw liybs DDKGGDG DDWVUGKDJGGIDW"
print(name[2])

print(name[4])

print(name[-1])
print(name[-2])

print(name[0])


hero = "Vijay Devarakonda"

for ch in hero:
    print(ch)
    # print(ch , end ="")



for ch in "Vijay Devarakonda":
    print(ch)
    # print(ch , end ="")

    
hero = "Vijay Devarakonda"

for ch in hero:   # 0,1,2,3,4
    if ch == " ":
        break
    print(ch)
    # print(ch , end ="")


hero = "Vijay Devarakonda"

for i in range(5):
    print(hero[i])



hero = "Vijay Devarakonda"

for i in range(len(hero)):
    print(hero[i])




# Slicing :  extracts a part of the string 

# string[start:stop:step]

# by default values 
# start - 0
# stop - end of the string
# step - 1

hero = "Vijay Devarakonda jhafjakhs jjgsacguaffajv iuugasgjavgc CLJLCjhafajhg ca"
print(hero[0:5])

print(hero[6:])

print(hero[:4:])

print(hero[:])

print(hero[::-1]) # reverse of a string 

print(hero[6:10])



# String formatting : allows inserting variables inside the strings dynamically 



# print(name," is a superman")

# Sairam is a superman 
# sreenadh is a superman 

# print("name is a Batman") # name is a Batman 

# python supports :

# f-strings  (latest)

#name = input("enter your name : ")
#age = int(input("enter your age : "))

# print(f"My name is {name} and I'm {age} years old.")


rice = 1500
atta = 500
veggies = 400
oil = 1000

print(f"total bill amount :{rice+atta+veggies+oil}")


name = "python training"
print(f"{name.upper()} is very easy.")

a = 5
print(f"square of a is : {a*a}")


# format() 

print("Welcome {}".format("Rocky"))

print("sum of numbers : {}".format(100+200+300+780+920))

print("{1} Welcome {0} {2}".format("Rocky" , "Good morning" ,"superman"))

print("Welcome {name} hi {jobrole}".format(name = "Rocky" , jobrole = "Trainer"))

'''

# % formatting (old style)

name = "sairam"
age = 29
print("my name is %s" %name)
print("my age is %d" %age)
print("my name is %s and my age is %d" %("Rocky",29))





