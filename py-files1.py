"""
File Manipulation
"""

# handle = open('romeo.txt')
# for line in handle:
   #You can rename the variable to change strip 
    # line = line.strip()
    #print(line)


###Fetch only the line with Arise
# handle = open("romeo.txt")

# for line in handle:
#     line = line. strip()

#     if line.startswith('Arise'):
#         print(line)


###Display other line apart from "arise"
# handle = open('romeo.txt')

# for line in handle:
#     line = line.strip()

#     # if not line.startswith('Arise'):
#     #     print(line)

#     if line.startswith("Arise"):
#         continue

#     print(line)





###Numbering Each line in a file
# handle = open('romeo.txt')
# counter = 0
# for line in handle:
#     counter = counter + 1 
#     line = line.strip()
#     print(counter, line)




### Retrieve each word in the line file

# handle = open("romeo.txt")

# for line in handle:
#     line = line.strip()
#     line = line.split()

    #print(line)
    #for word in line:
        #print(word)



###Number each word

handle = open("romeo.txt")
counter = 0

for line in handle:
    line = line.strip()
    line = line.split()


    #print(line)
    for word in line:
        counter = counter + 1
        print(counter, word)
      