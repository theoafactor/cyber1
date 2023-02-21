myName = "James"


##1. if block can exist 
if myName == "James":
    print("Welcome James")

##2. elif block can exist together with if alone
if myName == "James":
    print("Welcome James")
elif myName == "Jerry":
    print("You are welcome Jerry")

## 3 You cannot start conditional statements with elif or else 
elif myName == 'Jade':
    print("Jade")