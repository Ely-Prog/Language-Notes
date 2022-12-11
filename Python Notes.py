#Python Notes


# Data Types 


# True/False = Boolean 
# "Text " = String 
# 1 = int 
# 2.3 = float 


# Operators 

#  + = addition
#  - = Subtraction
#  * = Multiplication 
#  / = Division 
#  ** = Exponents 
#  // = division without remainder (64/10 = 6.4, 64//10 = 6)
#  %  = Gives only remainder (64/10 = 4)

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



# While loops 


print ("for this example, enter a number less then a second number, it will be incrementer until it is equal to the second number")

a = int(input())
b= int(input())

# while a < b:
#     print (a,"is not yet equal to",b,"number will be incremented by 1")
#     a+=1
#     if a == b:
#         print(a,"is equal to",b,"the incrementaion sequence will now break")
#         break

while a < b: 
    print (a,"is not yet equal to",b,"number will be incremented by please enter another number")
    a = int(input())
    


    if a == b: 
        print(a,"is equal to",b,"the incrementaion sequence will now break")
        break