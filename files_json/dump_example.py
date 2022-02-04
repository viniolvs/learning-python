"""
O módulo json (JavaScript Object Notation) permite descarregar estruturas de dados Python
simples em um arquivo e carregar os dados desse arquivo na próxima
vez que o programa executar.
"""
import json

filename = 'numbers.json'
numbers = list(range(1,10,2))


with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)