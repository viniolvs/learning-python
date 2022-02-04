"""
Formatando valores com modificadores

:s - Strings
:d - Inteiros
:f - Float

VAR :.(NUM)f - NUM = quant de casas decimais
VAR :(CARACTERE)(< ou > ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 11
print(f'{num_1:0>10}')

print(f'{num_1:0<10}')

print(f'{num_1:0^10}')

num_2 = 1.2579564785

print(f'{num_2:.3f}')

print(f'{num_2:0>10.2f}')

nome = 'Vinicius de Oliveira'

nome_formatado = '{:*^40}'.format(nome)
print(nome_formatado)

nome_formatado = '{n:&^40}'.format(n=nome)
print(nome_formatado)

nome = 'Vinicius'
sobrenome = 'de Oliveira'

nome_formatado = '{0:#>30} {1:@<30}'.format(nome,sobrenome)
print(nome_formatado)
