nomes = ["Maria", "Vini", "Luis", "Leo", "Maria Eduarda", "Dudi"]

for nome in nomes:
    print (f"Saudaçoes {nome}")
    
del nomes[0] #deleta o elemento 0 da lista


nomes_removidos = []
nome = nomes.pop() #remove o ultimo elemento da lista
nomes_removidos.append(nome)
nome = nomes.pop(0) #remove o elemento do indice 0
nomes_removidos.append(nome)
print(nomes)
print(nomes_removidos)

nomes = ["Maria", "Vini", "Luis", "Leo", "Maria Eduarda", "Dudi"]

removido = "Luis"
nomes.remove(removido) #remove por valor apenas a primeira ocorrencia
print("O nome " + removido + " foi removido")
