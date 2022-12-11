#Python Notes


# Data Types 

# \n = New Line
# True/False = Boolean 
# "Text " = String 
#int = 1 
#float = 2.3 
#List = [1,2,3] 
#Tuple = (255,255,255) / (2,3) used to store coordiantes or colour values 
#------------------------------------------------------------------------------------------------------------------------------------
# Operators 

#  + = addition
#  - = Subtraction
#  * = Multiplication 
#  / = Division 
#  ** = Exponents 
#  // = division without remainder (64/10 = 6.4, 64//10 = 6)
#  %  = Gives only remainder (64/10 = 4)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Conditions 
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


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# While loops 




#print ("for this example, enter a number less then a second number, it will be incrementer until it is equal to the second number")

#a = int(input())
#b= int(input())

# while a < b:
#     print (a,"is not yet equal to",b,"number will be incremented by 1")
#     a+=1
#     if a == b:
#         print(a,"is equal to",b,"the incrementaion sequence will now break")
#         break
#------------------------------------------------------------------------------------------------------------------------------
# while a < b: 
#     print (a,"is not yet equal to",b,"number will be incremented by please enter another number")
#     a = int(input())
    


#     if a == b: 
#         print(a,"is equal to",b,"the incrementaion sequence will now break")
#         break

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Condition is not needed, because its specified in the variable decalaration 

# loop = True

# while loop: 
#     inputs = input("give an input:")
#     if inputs == "stop":
#         break  (OR IN THIS CASE loop=False)





#--------------------------------------------------------------------------------------
# For Loops 


# For loops can take (Start,stop,increment) arguments 

# for x in range(0,12,2):
#     print (x)



#-----------------------------------------------------------------------------------------------------------------------------------------------------------
# For loops with lists 

# fruits = ["apples", "pears", "Strawberries"]

#for fruit in fruits: 
    #print (fruit) 

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



#-------------------------------------------------------------------------------------------



#LISTS

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

#----------------------------------------------------------------------------------------------------------------------------------------------------

#String Methods
#.strip() = removes all of leading and trailing white spaces OR CHARACTERS from string / let the _ = spaces.  "______hello____ " = "hello"

# text = input("input something please:")

# print (text.strip())


# .len() = returns the length of string or list 


# text = input("input something please:")
# print (len(text))


#.lower() = changes the case of string to lower case
# text = input("input something please:")
# print (text.lower())



#.upper() = changes the case of string to upper case
# text = input("input something please:")
# print (text.upper())


#.split = creates a list from a string, allows for an argument to be given which will use the value to seperate the list.

# text = input("input something please:")
# print (text.split("."))

# ----- Output ----
#  input something please: hello.tim.by.hi
# ['hello', 'tim', 'by', 'hi']


#--------------------------------------------------------------------------------------------------

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

#---------------------------------------------------------------------------------------------------------------------------------
#Functions 

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
#--------------------------------------------------------

# def areaOfRectangle(length,width):
#     area = length* width
#     return area


# print("Area of rectangle specified is", areaOfRectangle(5,6))


#----------------------------------------------------------------------------------------------------------------------

#File reading 

#Text Files must be saved in the same directory as the working directory.

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
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\

# File Writing  

# file = open("TestFile.txt", "w")      #Using "w" will overwrite the file with whatever is specified.

# file.write("python\n")
# file.write("I am learning how to write to a file")

# file.close()

#-------------------------------------------------------------------------------------------------------------------------------------------

#.find() and .count()

#can be used on strings and lists 

# string = "hello!"

# print(string.find("l") )             #this returns the indecy of the spefified letter, if not found the value -1 will be returned. Python will not use 0 because 0 is a valid index number
#                                      # If there is more then one character matching the requested search, python will only list the first found then stop.

# print(string.count("l") )            #Returns the number of characters in string


# ---------------------------------------------------------------
# string2 = input("please type something: ")
# if string2.count("_") > 0:                      #searches for _ if the count for _ is more then 0, it will say that it is found. 
#     print(string2.count("_"), "Underscores found")                            
# else:
#     print("'_' character not found")


#-----------------------------------------------------------------------------------------------------------------------------------------------------------
# Modules and Imports




