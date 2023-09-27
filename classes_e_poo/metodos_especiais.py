# O que são Magicdunder Methods (Métodos especiais)

class Pessoa:
    def __init__(self):
        self.nome = 'Sou uma Pessoa'
        self.habilidade = ['Habilidade 1', 'Habilidade 2', 'Habilidade 3']
    
    # Representacao para programadores 
    def __repr__(self):
        return f'classe Pessoa com propriedades nome e habilidade'
    
    # O que deve ser mensurado para determinar a quatidade daquela classe
    def __len__(self):
        return len(self.habilidade)
    
    def __str__(self):
        return f'{self.nome} com as habilidades {self.habilidade}'
    

pessoa = Pessoa()
print(pessoa.nome)
print(repr(pessoa))
print(pessoa)
