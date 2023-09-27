# Polimorfismo - Seja flexível
'''
class Carro:
    def ligar(self):
        print('Ligando o carro!')


class Moto:
    def ligar(self):
        print('Ligando a moto!')
        
# Polimorfismo:
def iniciar(veiculo):
    veiculo.ligar()
    

carro = Carro()
moto = Moto()

iniciar(carro)
iniciar(moto)
'''

# Polimorfismo
class Pessoa:
    def apresentar(self, nome, idade=None, profissao=None):
        if idade and profissao != None:
            print(f'{nome}, {idade}, {profissao}')
        elif idade != None:
            print(f'{nome}, {idade}')
        elif profissao != None:
            print(f'{nome}, {profissao}')
        else:
            print(f'{nome}')
            
pessoa = Pessoa()
pessoa.apresentar(nome='Joao', idade=22, profissao='Desenvolvedor')
pessoa.apresentar(nome='Emilly', idade=19)
pessoa.apresentar(nome='Emilly', profissao='Designer')
pessoa.apresentar(nome='Joao')
