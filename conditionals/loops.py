numbers = [1, 2, 3, 4, 5, 6, 7, 8]

students = [
        {
            "firstname": 'James',
            "lastname": "John",
            "email": "james@email.com",
            "id": 123
        },
        {
            "firstname": 'Jerry',
            "lastname": "Andrew",
            "email": "jerry@email.com",
            "id": 124
        },
        {
            "firstname": 'Mary',
            "lastname": "Joseph",
            "email": "mary@email.com",
            "id": 125
        },
        {
            "firstname": 'Jade',
            "lastname": "Henry",
            "email": "jade@email.com",
            "id": 126
        }

]

email = input("Enter your email address: ")


for student in students:
    if email == student["email"]:
        print("Welcome " + student["firstname"])
        break
else:
    print("You are not registered")




