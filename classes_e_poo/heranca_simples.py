# Herança

class Camera:
    # Construtor
    def __init__(self, marca, mega_pixels):
        self.marca = marca
        self.mega_pixels = mega_pixels
        
    def tirar_foto(self):
        print(f'Foto tirada com a camera da marca {self.marca} com a qualidade de {self.mega_pixels} megapixels')
    

class CameraCelular(Camera):
    # Contrutor
    def __init__(self, marca, mega_pixels, qtd_cameras):
        super().__init__(marca, mega_pixels) # Herdando os objetos da classe pai(Camera)
        self.qtd_cameras = qtd_cameras
        
    def aplicar_filtro(self, filtro):
        print(f'Aplicando filtro {filtro}')

    # Modificando funcao da classe pai(Camera)
    def tirar_foto(self, camera_a_utilizar):
        print(f'Foto tirada com a camera da marca {self.marca} com a qualidade de {self.mega_pixels} megapixels, utilizando a camera {camera_a_utilizar}')


class CameraSeguranca(Camera):
    def __init__(self, marca, mega_pixels, horas_minimas_de_gravacao):
        super().__init__(marca, mega_pixels)
        self.horas_minimas_de_gravacao = horas_minimas_de_gravacao
        
    def rotacao_camera(self, direcao):
        print(f'Rotacionando a camera para {direcao}')
        
        
camera_seguranca = CameraSeguranca('Sony', '16mp', 10)
camera_seguranca.rotacao_camera('direita')


print(issubclass(CameraCelular, Camera))
print(issubclass(CameraSeguranca, Camera))


# camera_celular = CameraCelular('Sony', '16mp', 4)
# camera_celular.aplicar_filtro('Azul')
# camera_celular.tirar_foto(2)
