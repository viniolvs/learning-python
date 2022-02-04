filename = 'write_example.txt'

"""
modos de abertura de arquivo
"a"  - Escreve ao final do arquivo; se este não existir, é criado
"r"  - Abre o arquivo para a leitura, se não existir, lançar um eerro de IOError
"r+" - Abra um arquivo para leitura e escrita. Se não existe, lança um erro IOError
"w"  - Abre um arquivo para escrita. Se existe, ele 'trunca' tudo e escreve por cima. Se não existir o arquivo, ele cria
"w+" - Abre para leitura e escrita. Se existe, apaga todo conteúdo e escreve por cima. Se não existir o arquivo, ele cria
"ab", "rb", "r+b", "wb", "w+b" - Abre arquivos para trabalhar com entrada e saída no modo binário, para plataformas Windows e Macintosh
"""

with open(filename, 'w') as file_object: 
    file_object.write("Wrinting on txt.")

with open(filename, 'a') as file_object: 
    file_object.write("Appending on txt.")
