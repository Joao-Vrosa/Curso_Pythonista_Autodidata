class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

# Instancias:
computadorUm = Computador('Acer', '8Gb', 'nvidia')
print(computadorUm.marca)
print(computadorUm.memoria_ram)
print(computadorUm.placa_de_video)

