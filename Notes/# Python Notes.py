# Python Notes





#NOTES FOR PUSHING AND COMMITTING 

#1. Stage changes by selecting the + in source control, then hit, the ... at top of source control
#2. next hit commit staged
#3. click the dots again,
#4. Select Push to..


# Data Types 

# \n = New Line
# True/False = Boolean 
# "Text " = String 
# int = 1 
# float = 2.3 
# List = [1,2,3] 
# Tuple = (255,255,255) / (2,3) used to store coordiantes or colour values 
# # # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Operators 

#  + = addition
#  - = Subtraction
#  * = Multiplication 
#  / = Division 
#  ** = Exponents 
#  // = division without remainder (64/10 = 6.4, 64//10 = 6)
#  %  = Gives only remainder (64/10 = 4)
# # # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Conditions 
# < Less than
# > Greater than 
# == Equal to 
# != - Not equal to 
# And = Both conditions must be true 
# or = if either conditions are true
# if not = if this condition is NOT true
# If else elif 

# print("please enter two numbers to compare")
# a = int(input())
# b = int(input())

# print("you chose the numbers",a,"and",b)


# if a > b: 
#     print (a, "is greater than",b)
    
# elif a==b:
#     print(a, "is equal to",b)
# else:
#     print (a, "is not greater then",b) 


# # # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# While loops 




# print ("for this example, enter a number less then a second number, it will be incrementer until it is equal to the second number")

# a = int(input())
# b= int(input())

# while a < b:
#     print (a,"is not yet equal to",b,"number will be incremented by 1")
#     a+=1
#     if a == b:
#         print(a,"is equal to",b,"the incrementaion sequence will now break")
#         break
# ------------------------------------------------------------------------------------------------------------------------------
# while a < b: 
#     print (a,"is not yet equal to",b,"number will be incremented by please enter another number")
#     a = int(input())
    


#     if a == b: 
#         print(a,"is equal to",b,"the incrementaion sequence will now break")
#         break

# # # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Condition is not needed, because its specified in the variable decalaration 

# loop = True

# while loop: 
#     inputs = input("give an input:")
#     if inputs == "stop":
#         break  (OR IN THIS CASE loop=False)





# --------------------------------------------------------------------------------------
# For Loops 


# For loops can take (Start,stop,increment) arguments 

# for x in range(0,12,2):
#     print (x)



# # # -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# For loops with lists 

# fruits = ["apples", "pears", "Strawberries"]

# for fruit in fruits: 
#     print (fruit) 

# for fruit in fruits:     
#     if fruit == "pears":
#         print (fruit)
#     else: 
#         print ("not pears")
 
# for x in range (0,6):               #This loop basically says, for every item, tried in this loop that will be run from (0,6) or 6 times.  if the current run through of the loop or x, is pears, say so. if not say not pears
#     if fruits[x] == "pears":
#         print (fruits[x])
#     else:
#         print ("not a pear")

# #  OR 
# for x in range (len(fruits)):               #This does the same thing, but specifies the amount or times the loop will run based on the length of the list itself.
#     if fruits[x] == "pears":
#         print (fruits[x])
#     else:
#         print ("not a pear")



# -------------------------------------------------------------------------------------------



# LISTS

# fruits = ["apple","orange",3] 
# print (fruits)
# # Indicies start at 0, -- apple = fruits[0], orange = fruits[2]
# print(fruits[0])

# #Append to list

# fruits.append("Strawberry")
# print(fruits)

# # Modifying Lists 
# fruits[2] = "bannanaranna"
# print (fruits)

# # # ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# String Methods
# .strip() = removes all of leading and trailing white spaces OR CHARACTERS from string / let the _ = spaces.  "______hello____ " = "hello"

# text = input("input something please:")

# print (text.strip())


# .len() = returns the length of string or list 


# text = input("input something please:")
# print (len(text))


# .lower() = changes the case of string to lower case
# text = input("input something please:")
# print (text.lower())



# .upper() = changes the case of string to upper case
# text = input("input something please:")
# print (text.upper())


# .split = creates a list from a string, allows for an argument to be given which will use the value to seperate the list.

# text = input("input something please:")
# print (text.split("."))

# ----- Output ----
#  input something please: hello.tim.by.hi
# ['hello', 'tim', 'by', 'hi']


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Slice Operator  - allows for a list of characters in strings to be outputed. StartValue:StopValue. Spaces count towards the value.  StartValue:StopValue:IncremenentValue

# fruits = ["apples","pear","strawberry"]
# text = "Hello I like python"
# print (text[0:9]) 
# print (text[2:5]) #This will start at 2 and end at 5
# print (text[:7]) # this will stop at the 7th character
# print (text[2:])  #This one will stop at the end of the string, but start at the 3rd(0,1,2)
# print (text[::2]) #this will print the whole string, but only read every second(third    ^) character.

# fruits [0:0] = "b" #this will instert B into the list at the first indecy
# print (fruits)
# fruits [1:1] = "b" #this will instert B into the list at the Second indecy
# print (fruits)
# fruits [2:2] = "b" #this will instert B into the list at the Third indecy
# print (fruits)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Functions 

# x = int(input("enter value for x: "))

# def addTwo(valueOfX):
#     return (valueOfX + 2)**2

#                                           #this function took a interger input as X, then defined a function, I gave an argument for the function (naming it whatever I want), then called the function
# print (addTwo(x))                                    

# addTwo(x)             #<--------------- calling function
# #---------------------------------

# def subTwo(number):
#     return number - 2


# y = subTwo(12)
# print (y)

# def printstring(string):
#     print(string)

# printstring("Hello")
# --------------------------------------------------------

# def areaOfRectangle(length,width):
#     area = length* width
#     return area


# print("Area of rectangle specified is", areaOfRectangle(5,6))


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# File reading 

# Text Files must be saved in the same directory as the working directory.

# file = open("TestFile.txt", "r")                  #specify File name, and what you would like to do "r" = read. This will display = ['Hello, this is a test file!\n', 'Coool\n', 'Graeat\n', 'adwad a\n', 'adwa dd']
# fileread = file.readlines()
# print (fileread)

# This is not the easiest way to read a file, however will allow for checking if a files first or last character is equal to a specific character
# newlist = []
# for line in fileread:
#     if line[-1] == "\n":                                             

#         newlist.append(line[:-1])                # This will loop through every line in the file, and "append" a negative character IF the line[-1] == \n
      
#     else: 
#         newlist.append(line)                         #this line commits changes to the list 

# print(newlist)


# newlist = []
# for line in fileread:
#     newlist.append(line.strip())

# print(newlist)                                     
# file.close()
# # # ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# File Writing  

# file = open("TestFile.txt", "w")      #Using "w" will overwrite the file with whatever is specified.

# file.write("python\n")
# file.write("I am learning how to write to a file")

# file.close()

# # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# .find() and .count()

# can be used on strings and lists 

# string = "hello!"

# print(string.find("l") )             #this returns the indecy of the spefified letter, if not found the value -1 will be returned. Python will not use 0 because 0 is a valid index number
#                                      # If there is more then one character matching the requested search, python will only list the first found then stop.

# print(string.count("l") )            #Returns the number of characters in string


# # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# string2 = input("please type something: ")
# if string2.count("_") > 0:                      #searches for _ if the count for _ is more then 0, it will say that it is found. 
#     print(string2.count("_"), "Underscores found")                            
# else:
#     print("'_' character not found")


# # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# import math
# import pygame
# import os 
# etc
# import math

# print (math.pi)


# # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# #Optional Perameters 

# def func(x, text='2'):                  #We can specify the default value of text, so if it is not specified, we can default to 2. running the function as is will use the else statement.
#     print(x)                             #If an argument is specified in defining the function, that argumnet is not NEEDED to make the function run. 
#     if text == 1: 
#         print ("number is 1.")

#     else:
#         print("number is not 1")

# # text = int(input ("please enter the number 1: "))
# func("hello This is the value for x\n" )             #We can uthe line 332 to change the value for text from the default.




# # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Try and Excpet 

#fore this example, we want the user to enter an interger without the program failing.

# text = input("Username: ")
# number = int(text)
# print (number)

#This would give an error message end end the progranm

# text = input("Username: ")
# try:                           #Try to do this 
#     number = int(text)
#     print (number)
# except:                         #If it doesnt work do this 
#     print ("Invaldid Username (Not a number)")      #At this point, it will print this line if the entered value cannot be converted into an interger. 

 # to cycle this through, try this = 


# a = True
# while a:
#     text = input("Username: ")
#     try:                            
#         number = int(text)
#         print (number)
#         a = False   #<----- or use break
#     except:                          
#         print ("Not an interger, try again")  
#         continue

# # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Global vs Local variables

#Global Variables = can be used anywhere in code 
# Local variables = can only be used within its method or class

# var = 9 
# loop = True

# def func(x):
#     newVar = 7                #The point of this code is to define the same function in multiple spots, and show that even if there is the same variable name, if a function is used it will only use the 
#     print(newVar)
#                                   # variable within the function
#     print(var)                     # <--- Note: Var can still be used in the function because it was declared outside of the method's scope. that is a global variable. 


#     if x == 5: 
#         return newVar

# def otherFunc():
#     newVar = 111
#     global loop             # <----- this line tells python to make the variable loop global, which overwrites the True value it has in line 378 with the value 7.
#     loop = 7
#     print (newVar)

# func(5)


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Objects

#Everything is an object, which belongs to  a method or class. Using an exmaple like this 

#print(x.upper())                 # The object type is a string, and the .upper is a method which belongs to the string class


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Classes 

#Creating Classes 


# Creating a class

#Classes cabne be created by tepiny class "classname"():
#inside of the brackets, we can define what the class will be. in this case object will be used 



# Methods 



#Defining the __init__ 

#what this does is automatically run the method __init__ every time. it is the initalization proccess for the class
#in this class, we must give self in the brackets as well as any other varibale we would like to use in the class.

#next, we use thge self.argument = arguemnt

#This says: for the instance that is being run. the instance's argument will = argument. Example: self.name = name

# using the example, whenever an instance of name is being used, it will belong to the instance that created it







# class Dog(object):        #Class is defined 
#     def __init__(self,name,age):         # Must be initalized for things in the class to happen. Things under this __init__ will happen everytime the class is called.
#                                 #also must give atrributes. Attrributes are given by using self. 
#         self.name = name            
#         self.age =  age
        

#     def speak(self):
#         print("Hi I am", self.name, "and I am", self.age)


#     def changeAge(self,age):
#         self.age = age


# ElyasSSS = Dog("Elyas",20)   # this will run an instance of the Dog class. ElyasSSS.name will be Elyas for this time (or instance ) Dog is called. all we are doing here is giving values to the parameters.
# Buddy = Dog("Buddiee",10)

# ElyasSSS.speak()            #in this line, we call  the speak method. Speak will display the self.name, and self.age which has been defined in the lines above
# Buddy.speak()

# ElyasSSS.changeAge(10000)      #Calling this will change the age to the defined parameter. 

# ElyasSSS.speak()

# print(ElyasSSS.age)               #This line will call the attribute specified.

#by using a name parameter in the init, it will mean that we have give a name argument when calling the Dog class. In line 422, when we say Elyas = Dog("elyas"), 
# the Self will refer to the instance or variable in this case. Basically, we are saying ElyasSSS.name = "Elyas"


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Atrribute inherritance 




# class Dog(object):       
#     def __init__(self,name,age):         
                                
#         self.name = name            
#         self.age = age
        

#     def speak(self):
#         print("Hi I am", self.name, "and I am", self.age)

# #This is an exmple of keeping the same attributes, this does NOT use inheritence!!!!

# class Cat(object): 
#     def __init__(self,name,age,colour):                      
#         self.name = name            
#         self.age = age
#         self.colour = colour

#     def speak(self):
#         print("Hi I am", self.name, "and I am", self.age)









# class Dog(object):       
#     def __init__(self,name,age):         
                                
#         self.name = name            
#         self.age = age
        

#     def speak(self):
#         print("Hi I am", self.name, "and I am", self.age)

#     def talk(self):
#         print("Bark!")



# class Cat(Dog):                     #uses another class as the argument in the parentheses. This will allow for all of the attributes of Dog to be hi
#     def __init__(self, name, age,colour):              #Method for init
#         super().__init__(name,age)                 #inits the attributes from dog 
#         self.colour = colour

#     def talk(self):                         #talk is in both cat and dog, but will be overwritten in the cat class becasue we redefined it
#         print("Meow!")


# thor = Cat("Thor",5,"Spotted")        #loading the class with attributes for the thor instance. 
# thorbrother = Cat("thorbrother",5,"Spotted")


# thor.talk()
# print(thorbrother.age)




# class Vehicle():
#     def __init__(self,price,gas,colour):
#         self.price = price
#         self.gas= gas
#         self.colour = colour 

#     def fillUpTank(self):
#         self.gas = 100

#     def emptyTank(self):
#         self.gas = 0
    
#     def gasLeft(self):
#         return self.gas


# class Car(Vehicle):
#     def __init__(self, price, gas, colour,speed):
#         super().__init__(price, gas, colour)
#         self.speed = speed

#     def beep(self):
#         print("Beep beep")


# class Truck(Car):
#     def __init__(self, price, gas, colour, speed):
#         super().__init__(price, gas, colour, speed)
#         self.speed = speed
#         self.tires = tires
    
#     def beep(self)
#         print("HONK HONK")
    

# class Motorcycle(Vehicle):

#     def __init__(self, price, gas, colour,helmet):
#         super().__init__(price, gas, colour)
#         self.helmet = helmet


#This example shows inherretence. in the example, All classes are inherriting (price,gas,colour) from the Vehicle class. The super Init allows for those to init.
#We can also inherrit from classes that are being inherrited. for example, Truck is inherriting from car, which is inherriting from Vehicle.

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Overloading methods 
# class Point():
#     def __init__(self,x=0 , y=0):
#         self.x = x
#         self.y = y
#         self.coords = (self.x,self.y)

#     def move (self,x,y):
#         self.x += x 
#         self.y += y

#     def __add__(self, p):
#         return Point(self.x +p.x, self.y + p.y)

#     def __sub__(self, p):
#         return Point(self.x - p.x, self.y - p.y)

#     def __mul__(self, p):
#         return self.x + p.x + self.y * p.y

#     def length(self):
#         import math
#         return math.sqrt(self.x**2 +self.y**2)


#     def __gt__(self,p):

#         return self.length() > p.length()

#     def __ge__ (self,p):
    
#         return self.length() >= p.length()

#     def __lt__ (self,p):

#         return self.length() < p.length()
   
#     def __le__ (self,p): 

#         return self.length() <= p.length()

#     def __eq__ (self,p):


#         return self.x == p.x and self.y == p.y



#     def __str__ (self):
#         return "(" + str(self.x ) +"," + str(self.y) + ")"



# p1 = Point(3,4)
# p2 = Point(3,2)
# p3 = Point(1,3)
# p4 = Point(0,1)
# p5 = p1 + p2 
# p6 = p4 - p1
# p7 = p2* p3


# print(p1==p2)
# print(p1 >= p2)
# print (p3 > p7)

# print(p5,p6,p7)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------a

#Static Methods and Class methods !!!!!!!!!
