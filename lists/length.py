# nums = [1, 2, 3, 4, 5]

# ## len() function 

# value = len(nums)

# print(value)

##
## create a list of users where the list contains just the firstname
## the firstnames will be collected using input() method

# -> exit the program when the length of the list reaches 3
users = []
while True:
    firstname = input("Enter your first name: ")
    users.append(firstname)
    print(users)
    if len(users) == 3:
        break