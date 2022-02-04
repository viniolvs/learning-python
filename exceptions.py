import string
#calculadora de divisao
while True:
    print("Give me two numbers and I'll divide them")
    print("Enter q to quit")
    
    first_number = second_number = ""
    while(not first_number or not second_number):        
        first_number = input("First number : ")
        if (first_number =='q'):
            exit()
        second_number = input("Second number : ")
        if (second_number =='q'):
            exit()
        if(not first_number or not second_number):
            print("Invalid input")
        
    
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("u cant divide by 0")
    else:
        print(answer)
     
    print()