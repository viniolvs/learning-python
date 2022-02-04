lista = [1, 3, 4, 5]
lista_2 = ['A', 'B', 'C', 'D' ,'E']
lista_3 = ['nome', 'numero', 'telefone']

print (lista)

#lista de listas
lista_foda = [lista, lista_2, lista_3]

print(lista_foda)

print(lista[:3])
print(lista_foda[0])

#funciona como append
lista_foda[0] += lista_2 
print(lista) #lista = lista_foda[0]

#cria uma lista utilizando funcao range
L1 = list(range(5,10+1))
print(L1)

#combinando L1 com laço for
for valor in L1:
    print(valor,end= ' ')
print('\n')

#Desempacotamento de listas
lista = ["Luiz", 'Joao', 'Maria', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n1, n2, n3, *outra_lista, ultimo = lista
print(n1, n2, n3)
print (outra_lista)
print(ultimo)

n1, n2, *_ = lista