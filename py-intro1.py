

"""
Variables && Expression

Introduction to Python Programming

"""



# fname= "Cascarr"
# middlename= "Ugoo"
# lname= "Ihesie"
# fulname= fname+" "+middlename+" "+lname

# print("Hello " + fulname +"!!!")

### Mathematical operation
# num1 =20
# num2 =15
# result= num1 + num2

# print(result)






###Define Val one,two, three and result
# num1 = 30
# num2 = 40
# num3 = num1 * num2

# result = num1 + num2 + num3
# print(result)

# num1 = "25"
# num2 = 30
# result = int(num1) + num2

# print(result)


##Processing  User Input

#userInp = input("Whats your name? ")

#print("Oh, Welcome "+ userInp)







##Arithmetic Precedence

#solv = ( 2 + 2 ) * 4/2

#print (solv)



#num1 = input ('what is your age?: ')

#num2 = input ('what is your date of birth: ')

#cov_num1 = int(num1)

#cov_num2 = int(num2)

#result = cov_num1 + cov_num2

#print (result)





"""
Conditional Excecution
"""




##0ne way implementattion#


# known_user = 'Cascarr'

# if ( "Cascarr" == known_user ):
    
#     print ("Hello " + known_user )






##If i cant buy bread due to lack of fund i can just buy meat pie
##

# initial_pay = 2500

# increase_pay = initial_pay + 500

# if ( increase_pay >= 3000 ):
    

#     print ("just promoted")

# else: 
#     print ("junior employee")

# print('not there')







##prompt the user to enter value with condition

# num1 = int( input('Enter val1: ') )

# num2 = int( input('Enter val2: ') )

# result = num1 + num2

# if (result == 20):
#    print("win")

# else:
#     print ("Not win")







##What if we want the computer to give different reponse to different user and throw back unknown to unknown user

#user1 = 'cascarr'
#user2 = 'abdul'
#user3 = 'austin'

#if (user1 == "cascarr"):
    #print ("hello " + "cascarr")

#elif (user2 == "abdul"):
    #print ("hi hi " + "abdul")

#elif (user3 == "austin"):
    #print ("oh hello " + "austin")

#else:
    #print("unknown")








##what if i want to create a different response to the user if he speak different language
# user1 = input('name: ')
# lang = input('language: ')

# if user1 == "cascarr" and lang == "en":
#     print("hello " + user1)

# elif user1 == "cascarr" and lang == "es": 
#      print ("Hola "+ user1)

# else:
#     print ("language unidentified")








##when integer cannot properly convert words error handling is applied
# num1 = input("val1: ")
# num2 = input("val2: ")

# try:
#     #
#     conv_num1 = int(num1)
#     conv_num2 = int(num2)


#     result = conv_num1 + conv_num2

#     print(result)

# except:
#     print("error somewhere")


"""
Take Home Excercise 
Varriable, Expression and Expression
"""


##writing a program that uses input to prompt a user for their name and welcome them

#user1 = input("Enter your name: ")

#print ('Welcome ' + user1)







##Writing a program that prompts the user for hours and rate per hour to compute gross pay

#hour = input("Total Hours Worked:")
#rate = input("Rate Per Hour:")

#conv_hour = int(hour)
#conv_rate = int(rate)

#result = conv_hour * conv_rate

#print (result)






##Writing the value of the expression and the type of the value of the expression

#width = 17
#height = 12.0

#result = width/12.0 

#print(result)

#result = height/3

#print(result)

#result = 1 + 2 * 5 
#print (result)







##writing a program that prompts the user for a Celsius temperature and converts the temperature to fahrenheit

#celsius = input("Temperature:")

#conv_celsius = int(celsius)

#fahrenheit = conv_celsius * 1.8 + 32

#print (fahrenheit)





"""
Take Home Excercise
Conditional Excecution
"""




##Rewriting your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours
#
#normal_rate = int(input("Pay: ") ) 
#total_hours = int(input("Hours: ") )
#overtime_rate = (1.5)


#normal_pay = normal_rate * total_hours
#increase_pay = (total_hours - 40) * (overtime_rate * normal_rate)
#overtime_pay = normal_pay + increase_pay


#if (total_hours > 40):
    #print (overtime_pay)
#

#elif (total_hours <= 40):
    #print (normal_pay)








##Rewriting a program using try and except so that your program handles non-numeric input by printing a message and exiting the program

#num1 = input("Enter Hours: ")
#num2 = input("Enter Rate: ")
#

#try:
    #conv_num1 = int(num1)
    #conv_num2 = int(num2)

    #result = conv_num1 + conv_num2

    #print (result)

#except:
    #print ("Error, Please enter numeric input")









##Writing a program to prompt for a score between 0.0 and 1.0. if the score is out of range, print an error message, if the score is
#within range, print a grade

# user = input("Score: ")
# conv_num = float(user)

# if conv_num > 1.0:
#     print("Bad Score")

# if (conv_num >= 0.9):
# #if (conv_user > 90):   
#     print ("A")

# elif (conv_num >= 0.8):
# #elif (conv_user > 80):   
#     print ("B")

# elif (conv_num >= 0.7):
# #elif (conv_user > 70):
#     print ("C")

# elif (conv_num >= 0.6):
# #elif  (conv_user >= 60):
#     print ("D")

# elif (conv_num < 0.6):
# #elif (conv_user < 60):    
#     print ("F")



# else:
#     print ("Error")
   














