"""
While <condicao>:
    <codigo>
"""

x=10
while x:
    print(x)
    x-=1
print("End")


while x<=10:
    if x==4 or x==6:
        x+=1
        continue #passa para a prox repetição do laço
    print(x)
    x+=1
print("End")

while x<=10:
    if x==4 or x==6:
        break #Sai do laço
    print(x)
    x+=1
print("End")

"""
exemplos for
"""
texto = 'Vinicius'
for letra in texto:
    print(letra)

"""
Funcao range(start=0, stop, step=1)
"""
for n in range(10):
    print (n)

for n in range(5,50,5):
    print (n)
