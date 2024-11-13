"""
Function in Python Programming
"""

#def intro():
   # print("welcome to function programming!")
    #print("now you are programming programming!")
    #print("keep programming!")


##function Call


def login():
    user = "Cascarr"
    print("Hello " + user)
    print("Welcome to my System")

#login()


def myadd():
    num1 = 3
    num2 = 5
    result = num1 + num2
    print("output: " + str(result))

#myadd()

def mysub():
    num1 = 20
    num2 = 10
    result = num1 - 10
    print("total: " + str(result))

#mysub()

def mymulti():
    num1 = 25
    num2 = 25

    result = num1 * num2 
    print("Total: " + str(result))

# mymulti()


###Parameters and Argument

def intro(user, usemail):
    username = user
    print("Welcome " + username + "!\nYour Email is: " + usemail)

# intro("Cascarr", "c.ihesie45n1l@gamil.com")



"""
user lingual function
"""
def lingual(user, lang):

    ##
    if lang == 'en':
        print("Hello " + user)
    
    elif lang == 'fr':
        print("Bonjour " + user)

    elif lang =='vn':
        print("Xin chao " + user)

    elif lang == 'es':
        print("Hola " + user)

    else:
        print("unknown!")

#call
#lingual("Cascarr", "vn")

##function that accepts 2 arguments and handles the sum of the values

def myadd(para1, para2):
    result = para1 + para2
    print("Total: " + str(result))

##myadd(15, 3)






### A Calculator
def calc(para1, para2, opera):

        ## Conversion
    try:

        para1 = int(para1)
        para2 = int(para2)

    
        #check op
        if  opera == "+":
            result = para1 + para2
            print ("result: " + str(result))

        elif opera == "-":
            result = para1 - para2
            print ("result: " + str(result))
        

        elif opera == "*":
            result = para1 - para2
            print ("result " + str(result))

        elif opera == "/":
            result = para1 - para2
            print ("result " + str(result))

        else:
            print ("unknown!")
    
    except:
        print ("Error Somewhere")


#input funtionality
# usInp1 = input("Enter val1: ")
# usInp2 = input("Enter Val2: ")
# usInp3 = input("Enter Operator: ")


#Function Call

#calc(num1,num2,usInp3)
#calc(usInp1, usInp2, usInp3)
        








"""
Take Home Excersie
Function
"""


##1. What is the purpose of the Def Keyword in Python?

#b. It indicates the start of a funtion






##2. What will the following Python program print out

# def fred():
#     print("Zap")

# def jane():
#     print("ABC")

# jane()
# fred()
# jane()

#ABCZapABC





##3. Rewriting the grade program from the previous chapter using a funtion 
##called computegrade that takes a score as its parameter and returns a 
##grade as a string

def computegrade (grade):
  #perfect = grade
   try:
       
           #
       if (grade <= 1.0 and grade >= 0.9):   
            print ("A")
    
       elif (grade < 0.9 and grade >= 0.8):  
            print ("B")
       
       elif (grade < 0.8 and grade >= 0.7):
            print ("C")

       elif (grade < 0.7 and grade >= 0.6):
            print ("D")

       elif (grade < 0.6):
            print ("F")
        
    #    elif (grade == "Perfect"):
            # print ("Bad Score")
    
       else:
            print ("Bad Score")

   except:
        print("Bad Score")

# computegrade("perfect")









##Rewriting a pay computation with a time and the half for overtime and
##create a function called computepay which takes two parameter(hours and rate.)


def computepay(hours, rate):

    overtime_rate = 1.5
    result = hours * rate * overtime_rate
    print("Overtime Pay: " + str(result))

    userInp1 = input("Hours: ")
    userInp2 = input("Rate: ")
    print("Overtime Pay: " + str(result))

# computepay()







def addition():
   result = 5 + 5
   return result

# print(addition())





def calc(para1, para2, opera):

        ## Conversion
    #try:

        para1 = int(para1)
        para2 = int(para2)

    
        #check op
        if  opera == "+":
            result = para1 + para2
            return result
            # print ("result: " + str(result))

        elif opera == "-":
            result = para1 - para2
            return result
            # print ("result: " + str(result))
        

        elif opera == "*":
            result = para1 - para2
            return result
            # print ("result " + str(result))

        elif opera == "/":
            result = para1 - para2
            return result
            
#input funtionality
# usInp1 = input("Enter val1: ")
# usInp2 = input("Enter Val2: ")
# usInp3 = input("Enter Operator: ")


#Function Call
#print(calc(50,50,"+"))
     
#calc(usInp1, usInp2, usInp3)