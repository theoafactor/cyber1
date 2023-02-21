user = {
    "firstname" : "James",
    "lastname": "John",
    "age": 27, 
    "ranks": ["beginner", "intermediate", "senior", "most-senior"],
    "location": {
        "country": "Nigeria",
        "state": "Lagos",
        "street": "Oweh",
        "house_number": "2",
        "local_government_area": "Yaba" 
    },
    "phone": None,
    "education": {
        "level": "college",
        "degree": "BSc",
        "preferences": ("writing", "clubbing", "speaking")        
    }

}

# Answers
# 1. int()
user["location"]["house_number"] = int(user["location"]["house_number"])  #typecasting

# 2. 
user["phone"] = "01"

# 4. 
user["education"]["preferences"][len(user["education"]["preferences"]) - 1] = "reading"

# 6
user["age"] = str(user["age"])




# 1. change the data type of the user's house number to integer
# 2. change the phone of the user 
# 3. What type of data is "preferences" key pointing to?
# 4. update the the last item in the preferences***
# 5. What is the formula for getting the last item in preferences?
# 6. Change the age of the user to a string data type

# Loops and List 
