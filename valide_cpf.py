while True:
    print("\nDigite 0 para encerrar!")    
    input_cpf = ''
    while len(input_cpf) < 11:
        input_cpf = input("Digite um CPF: ")
        if(input_cpf == '0'):
            exit()

    cpf=''
    for i,dig in enumerate(input_cpf):
        if (dig!='.' and len(cpf)<9):
            cpf += dig
        
    digito_1 = 0
    for dig,i in enumerate(range(10,1,-1)):
        digito_1 += int(cpf[dig])*i

    digito_1 = 11 - (digito_1 % 11)
    if digito_1>9:
        digito_1 = 0

    cpf += str(digito_1)
    digito_2 = 0
    for dig,i in enumerate(range(11,1,-1)):
        digito_2 += int(cpf[dig])*i

    digito_2 = 11 - (digito_2 % 11)
    cpf += str(digito_2)

    if((int(input_cpf[len(input_cpf)-2]) == digito_1) and ((int(input_cpf[len(input_cpf)-1]) == digito_2))):
        print("CPF válido!")
    else:
        print("CPF inválido!")
