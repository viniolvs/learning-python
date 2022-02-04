while True:
    print("Enter q to quit:")
    n1 = input("Primeiro numero: ")
    if (n1 == 'q'):
        exit()
    n2 = input("Segundo numero: ")
    if (n2=='q'):
        exit()

    try:
        int(n1)
        int(n2) 
    except ValueError:
        print("Entrada inválida")
    else:
        print("Sum = ", n1 + n2)