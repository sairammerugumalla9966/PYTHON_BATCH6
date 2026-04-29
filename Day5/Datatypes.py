# what is a datatype ??

# what kind of data it is and what operations can be performed on it 

# Dynamic typing ---> no need to declare the datatype for the variables 

# built in datatypes 

# Numeric datatype ---> int , float , complex 
# intergers --->_ve , 0 , +ve 
# float ---> decimal point 
# complex --> imaginary numbers (3+4j)


# sequence datatype ---> string , list , tuple 
# string ---> ' ' , " " , """   """
# list ---> 
# tuple --->

# set datatype --> set
# mapping datatype ---> dictonary 
# Boolean datatype ---> True , False (true ,false)

'''
# collection datatypes ---> list , tuple , set , dictionary

name = "sairam"
print(type(name)) 

a = 10 
print(type(a)) 


statement = True
print(type(statement)) 

statement = False
print(type(statement)) 

print(msg)
print(type(msg))


numbers = 1,2,3,4,5
print(type(numbers))   # implicit conversion ---> python automaticallly converts the datatype 

age = "29"
print(type(age)) 

print(type(10/2)) #--> 5.0 float 

# explicit conversion ---> user converts the datatype manually

data = int(input("ask something : ")) # string datatype 
print(type(data))
print(data * 2)

data = float(input("ask something : ")) # string datatype 
print(type(data))
print(data * 2)

'''
# collection datatypes ---> these are containers used to store multiple items in a single variable 

# list --->[] , ordered, mutable sequence, allow duplicate values, different datatypes 

student = ["Rocky","trainer",29,100000.00,True]
student.append("super man")
print(student)

student.remove("super man")
print(student)

student.insert(1,"star man")
print(student)

print(student[1])

# mutable means it can change 

name = "Rebal star" # index (0  , n-1) 

# Nested list

students = [["Rocky",100],["praboos",99],["power star",101],["bhrami",98]]
print(students)

print(students[0][0])

print(dir(student))


name = "sairam"

names = "Rocky","shiva", "pavan", "narasimha","srinath","uday",90,167.898,True
print(names)
print(type(names))


# tuple ---> (), hetrogenous data ,allows duplicate values , 
# ordered collection ,indexes ,immutable sequence(doesnot create new objects means it can not be changed)

location =(178.99767 ,198.988464) # coordinates 

names = ("Rocky","shiva","pavan","narasimha","srinath","uday",90,167.898,True ,"narasimha","srinath","uday")
print(dir(names))
print(type(names))
print(names[0])


# set ---> {},unordered collection , doen not allow duplicate values , mutable , no indexes

id = {101,102,103,104,104,104,105,105,"sairam"}
print(dir(id))


names = ("Rocky","shiva","pavan","narasimha","srinath","uday",90,167.898,True ,"narasimha","srinath","uday")
print(set(names))
print(names)

ids = [101,101,102,103,104,104,105,105,"sairam"]
result =set(ids)
print(result)

print(ids)

id = {101,102,103,104,104,104,105,105,"sairam"}
print(dir(id))

# dictionary  : key-value pair , mapping datatype ,ordered collection , mutable ,

dic = {
      "name" : "sairam", 
       "job":"trainer",
       "age":29,
       "salary":50000
       }

print(dic.get("sairam"))
print(dic.get("name"))

print(dic.keys())
print(dic.values())

dic.update({"age" : 24})
print(dic)



