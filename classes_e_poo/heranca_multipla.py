# Herança Múltipla

class Pessoa:
    nome = 'Sou uma Pessoa'
    
    def convidar(self):
        print('Pessoa, vamos ao evento?')
        

class Proficional:
    nome = 'Sou um Proficional'
    
    def convidar(self):
        print('Proficional, vamos ao evento?')
        
        
class AtorProficional(Pessoa, Proficional):
    pass


ator_proficional = AtorProficional()
ator_proficional.convidar()
print(AtorProficional.mro())

