#cria uma lista com os 10 primeiros quadrados
squares = []
for value in range(1,11):
    squares.append(value**2)
print(*squares,sep=', ')

#tambem cria uma lista com os 10 primeiros quadrados
"""
Para usar essa sintaxe, comece com um nome descritivo para
a lista, por exemplo, squares. Em seguida, insira um colchete de abertura
e defina a expressão para os valores que você quer armazenar na nova
lista. Nesse exemplo, a expressão é value**2, que eleva o valor ao
quadrado. Então escreva um laço for para gerar os números que você quer
fornecer à expressão e insira um colchete de fechamento. O laço for nesse
exemplo é for value in range(1,11), que fornece os valores de 1 a 10 à
expressão value**2.
"""
squares2 = [value**2 for value in range(1,11)]
print(*squares2,sep=', ')