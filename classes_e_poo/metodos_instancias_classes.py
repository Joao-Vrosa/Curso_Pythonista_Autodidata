# Metodos comuns
# Metodos de Classes (Class Methods)
# Metodos estaticos (Static Methods)

class Computador:
    sistema_operacional = 'Windows 10'
    
    def __init__(self, marca, memoria_ram, placa_de_video):
        # Objetos:
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
    
    # Metodos comuns
    def exibir_dados(self):
        print(f'Marca: {self.marca}\nMemoria RAM: {self.memoria_ram}\nPlaca de Video: {self.placa_de_video}')
    
    # Metodos de Classes
    @classmethod
    def computador_escritorio(cls, memoria_ram):
        return cls('Dell', memoria_ram, 'Placa de Video - Baixo Custo')
    
    @classmethod
    def computador_gamer(cls, memoria_ram):
        return cls('Acer', memoria_ram, 'Placa de Video - Alto Custo')
    
    # Metodos estaticos
    @staticmethod
    def roda_programas_pesados(memoria_ram):
        if memoria_ram >= 8:
            return True
        else:
            return False


# Instancias:
computadorUm = Computador.computador_escritorio('4Gb')
computadorUm.exibir_dados()
print(computadorUm.roda_programas_pesados(4))

print('-----------------------')

computadorDois = Computador.computador_gamer('16Gb')
computadorDois.exibir_dados()
print(computadorDois.roda_programas_pesados(16))
