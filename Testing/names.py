from name_function import get_formatted_name

print("Enter q to quit: ")
while True:
    first = input("First name: ")
    if (first =='q'):
        exit()
    last = input("Last name: ")
    if (last == 'q'):
        exit()

    print(get_formatted_name(first, last))