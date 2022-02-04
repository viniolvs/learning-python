from importlib.resources import contents

#python só grava strings em arquivos de texto
#with fecha o arquivo após a identaçao
#open retorna um objeto q representa o arquivo em file_object
#contents é uma string q armazena tudo lido no arquivo 

filename = 'pi_digits.txt' 
#with open('/home/vinicius/Documentos/Programas/Python/files/pi_digits.txt') as file_object:
try:
    with open(filename) as file_object: 
        contents = file_object.read()
except FileNotFoundError:
    print("The file " + " doesn't exists")
else:
    print(contents)
"""
with open(filename) as file_object: 
    for line in file_object:
        print (line.rstrip()) #rstrip(remove linhas em branco)

with open(filename) as file_object: 
    lines = file_object.readlines() #armazana cada linha em uma lista
print('\n')
print(lines)
"""

