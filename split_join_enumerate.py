#Split - Dividir uma string
#Join - Juntar uma lista em uma string
#Enumerate - Enumerar elementeos da lista

string = "O Brasil é o pais do futebol."
lista = string.split(' ') #divide uma string baseado no parametro
for valor in lista:
    print (valor)

string_2 = ', '.join(lista)
print(f"string_2: {string_2}")

for indice, valor in enumerate(lista):
    print(indice, valor)

lista_2 = [ 
    [0, "Luiz"],
    [1,"HUlk4"],
    [2, "Otario"],
]

for indice, nome in lista_2:
    print (indice, nome)

print(lista_2[0][1])
