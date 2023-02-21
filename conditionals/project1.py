user = {
    "firstname": "James",
    "lastname": "Jerry"
}

print("Welcome to our Platform!")

## ask the users for their first name and last name
firstname = input("Enter your firstname: ")
lastname = input("Enter your lastname: ")

if firstname == user["firstname"] and lastname == user["lastname"]:
    print("You are registered")
    print("Welcome " + user['firstname'] + " " + user["lastname"])
else:
    print("This user is not registered")
    

