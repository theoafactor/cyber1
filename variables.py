## Data Types
# 1 String ' ', " " , ''' ''', """ """
myName = "James John"
# print(type(myName))

# 2. Number
# - float 
# - integer
myAge = 12.0
# print(type(myAge))

# 3. Boolean
# True | False
hasUserRegistered = True

# print(type(hasUserRegistered))

# 4. List [] - mutable
writingMaterials = ["pen", "eraser", "jotter"]

# # writingMaterials[0] = "biro"
# # writingMaterials[1] = "textbook"
# # writingMaterials[2] = "divider" 

i = 0
while i < len(writingMaterials):
    if i == 0:
        writingMaterials[i] = "Biro"
    if i == 1:
        writingMaterials[i] = "Text"
    
    if i == 2:
        writingMaterials[i] = "Divider"
    
    i = i + 1

print(writingMaterials)


registeredUsers = ["James", 'Jerry', "Andrew", "Mary", "Jacob"]
n = len(registeredUsers)
registeredUsers[ n - 1]
