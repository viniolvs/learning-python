"""
def funcao(<parametros>):
    #codigo
    return <retorno>
"""
#Valores padrões como parametros caso nenhum seja passado
def saudacao(msg="Ola", nome = "usuario"): 
    print(msg,nome)
saudacao()
saudacao("Oi", "Luiz")

def soma(a,b):
    return a+b
print(soma(5,7))


#Funcao retorna funçao 
def f(txt):
    print(txt)   
def dumb():
    return f
dumb()('Locura total')#chama dumb e executa f com o segundo parenteses)
var = dumb() #var = f
var("meu deus") 

#retorna uma tupla
def dumb2():
    return(1,2,3,4)
var = dumb2()
print(var,type(var))

#recebe uma tupla
#tuplas não podem ser alteradas
def func(*args, **kwargs):
    print (args)
    print(kwargs)
    print(kwargs["nome"])
    print(kwargs.get("nome")) #mais seguro, evita erro
    
lista = [1,2,3,4,5]
lista2 = [5,4,3,2,1]
func(*lista, *lista2, nome="Vinicius",sobrenome="Olivera")
