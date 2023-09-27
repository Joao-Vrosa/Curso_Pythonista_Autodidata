class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        # Objetos:
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video
        
    # Metodos da classe:
    def ligar(self):
        print('Ligando o computador!')
        
    def desligar(self):
        print('Desligando o computador!')
        
    def exibir_dados(self):
        print(f'Marca: {self.marca}\nMemoria RAM: {self.memoria_ram}\nPlaca de Video: {self.placa_de_video}')
        

# Instancias:
computadorUm = Computador('Acer', '8Gb', 'nvidia')

computadorUm.ligar()
computadorUm.desligar()
computadorUm.exibir_dados()
