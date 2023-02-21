

## create a list of users where the list contains just the firstnames
users = ["James", "John", 'Jerry']
## the firstnames will be collected using input() method

## check if the user's firstname entered is in the list
# -> if the user entered the correct firstname, the program should exit with a "Welcome" message
# -> exit the program if the user entered the wrong firstname thrice (exit with a 'You are not registered' message)
lives = 0
while True:
    firstname = input("Enter your first name: ")
    
    if firstname in users:
        print("Welcome")
        break
    else:
        print("Invalid name, please try again")
        lives = lives + 1
        if lives == 3:
            print("You are not registered")
            break
    