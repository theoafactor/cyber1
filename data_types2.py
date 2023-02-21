user = {
    "firstname": "James",
    "lastname" : "Jerry",
    "email": "james@email.com",
    "age": 12,
    "ranks": [
        {
        "name": "entry",
        "id": '1',
        "max": "4"
    }, 
    {
        "name": "junior",
        "id": '2',
        "max": "3"

    }, 
    {
        "name": "mid",
        "id": '3',
        "max": "2"
    }, 
    {
        "name": "senior",
        "id": '4',
        "max": "1"

    }]
}

print(user["ranks"][1]['name'])
print(user["ranks"][3]["max"])
