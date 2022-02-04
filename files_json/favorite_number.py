import json
filename = 'favorite_number.json'

try:
    with open(filename,'r') as file_obj:
        fav_number = json.load(file_obj)
except FileNotFoundError:
    pass
else:
    print("your favorite number is ",fav_number)
    exit()

try:
    fav_number = int(input("What's your favorite number?"))
except ValueError:
    print("That's not a number!")
else:
    with open(filename, 'a') as file_obj:
        json.dump(fav_number, file_obj)

