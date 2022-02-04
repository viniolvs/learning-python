from hashlib import new


alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color']) #printa 'green'

"""
Se um jogador atingir esse alienígena, podemos consultar quantos pontos
ele deve ganhar
"""

new_points = alien_0['points']
print("You earned " + str(new_points)+ " points!")

print(alien_0)
#adiciona novos pares chave-valor no dicionario
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#criando um dicionario vazio
alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 10
print(alien_1)

#modificando um valor
alien_1['color'] = 'yellow'
print(alien_1['color'])

#percorrendo dicionario com laço