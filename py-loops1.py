
"""
Loops and Iteration
"""




"""
Indefinite Loop
"""

# num = 1

# while num <= 5:
#     print(num)
#     num = num + 1



# Increment loop
 
# num = 1
# while num <= 15:
#      print(num)
#      num = num + 1



# Decrement loop

# num = 20
# while num >= 0:
#     print(num)
#     num = num - 1



#User input with Loop and Break and Continue

# while True:
#      data = input("names: ")
#      if data == "stop":
#         break




"""
Definite Loop
"""
# names = ("Cascarr", "Abdul", "Austin", "Greg", "Fatima", "Ahmad")

# for (i) in names:
#     print(i)


# items = (3,2,5,15,18,25,11,7,4)

# largest_num = 0

# for num in items:
#     if num > largest_num:
#         largest_num = num

# print("largest: " + str(largest_num))

# smallest_num = 50

# for num in items:
#     if num < smallest_num:
#         smallest_num = num
# print("Smallest: " + str(smallest_num))


##Another Way of finding the smallest num
# smallest_num = None
# for num in items:
#     if smallest_num is None:
#         smallest_num = num
    
#     elif num < smallest_num:
#          smallest_num = num

# print("Smallest: " + str(smallest_num))




##Class Work
##Print the 1st 10 natural number while using loop

# num = 1
# while num <= 10:
#      print(num)
#      num = num + 1


#2. Class work
#Write a program to accept a number from a user and calculate the sum of all numbers

# while True:
#      userInp = input("Enter Value: ")
#      if  userInp == "stop":
#         break

    #  conv_num = int(userInp)
    #  total = total + conv_num

    #  print(total)
      
    

##
# count = 0
# names = ("Cascarr", "Abdul", "Austin", "Greg", "Martins")

# for name in names:
#     count += 1
#     print(count, name)






###Write a program which repeatedly reads numbers until the user enters "done". 
# Once "done" is entered, print out the total, count, and average of the numbers,
# if the user enters anything other than a number, detect their mistake using try
#  and except and print an error message and skip to the next number


while True:
 try:
    userInp = input("Enter a Number: ")
    conv_num = str(userInp)
    if userInp == "done":
        break
 
 except:
    print("Invalid input") 