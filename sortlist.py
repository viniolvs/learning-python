cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort() #ordena de forma permanente 
print(cars)
cars.sort(reverse=True)#ordena de forma inversa
print(cars)

#a funçao sorted retorna a lista ordenada mas nao altera a lista original
cars = ["bmw", "audi", "toyota", "subaru"]
s = sorted(cars)
print(s)
print(cars)

cars.reverse()#inverte a lista
tamanho_lista = len(cars)