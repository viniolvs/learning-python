
palavra_chave = 'alemanha'
digitadas = []
erro = 5

while True:
    letra = input('Digite uma letra, você pode errar apenas 5 vezes!: ')
    letra = letra.lower()

    if(len(letra)!=1):
        print("Isso não vale cabeção, digite apenas uma letra.")
        continue


    if letra in palavra_chave:
        print(f'Acerto mizerave, a letra "{letra}" existe na palavra')
        digitadas.append(letra)
    else:
        print(f'A letra "{letra}" não existe na palavra')
        erro-=1

    aux = ''
    for letra_chave in palavra_chave:
        if letra_chave in digitadas:
            aux += letra_chave
        else:
            aux += '*'
    
    print (aux)
    if (aux == palavra_chave):
        print ("BOA MONSTRO")
        break
    elif(erro == 0):
        print("Seu merda, perdeu otário kkkkkkkk")
        break


