
# *args -> Quantidade variavel de argumentos
def somar(*valores, b):

    for valor in valores:
        b += valor
    print(b)
    

somar(1, 2, 2, b=15)

##


# Kwargs(Keyword arguments)
def concatenar(**palavras): ## ** -> Usar quando queremos utilar uma quantidade infinita de argumentos nomeados
    frase = ''
    for palavra in palavras.values(): ## .values -> Acessando os valores que foram passados para a tupla        
        frase += palavra + ' '
    print(frase)
        

concatenar(a='Somos', b='Pythonistas', c='Proficionais')
