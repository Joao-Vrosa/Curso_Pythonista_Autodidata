'''from datetime import datetime

def depositar_dinheiro():
    print('Depositando dinheiro!')
    
    def depositando_dolar():
        print('Depositando dolar!')
        
    def depositando_reais():
        print('Depositando reais!')
        
    depositando_dolar()
    depositando_reais()
    
depositar_dinheiro()'''

## Decorators

'''def meu_decorator(funcao):
    def wrepper():
        print('Antes!')
        funcao()
        print('Depois!')
    return wrepper

def parabenizar():
    print('Parabens!')
    

resultado = meu_decorator(parabenizar)
resultado()'''

from datetime import datetime

def monitorar_horario(funcao):
    def monitor():
        print(datetime.now())
        funcao()
        print(datetime.now())
    return monitor

@monitorar_horario
def baixar_musicas():
    print('Baixando musicas!')
    
baixar_musicas()