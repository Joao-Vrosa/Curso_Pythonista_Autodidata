# Classes Abstratas

from abc import ABC, abstractmethod

'''
class Camera(ABC):
    @abstractmethod
    def definir_tamanho_lente(self, tamanho):
        pass
    
    
class CameraProficional(Camera):
    def definir_tamanho_lente(self, tamanho):
        print(f'Alterando lente para o tamanho {tamanho}')
        
        
camera_proficional = CameraProficional()
camera_proficional.definir_tamanho_lente(5)
'''

class Monitor(ABC):
    @abstractmethod
    def aumentar_claridade(self, qtd_aumenta):
        pass
    
    @abstractmethod
    def diminuir_claridae(self, qtd_diminui):
        pass
    
# Todas as classes que herdarem a classe pai, devem implementar os seus metodos abstratos.
class MonitorFullHD(Monitor):
    def aumentar_claridade(self, qtd_aumenta):
        print(f'Aumentando a claridade em {qtd_aumenta} pontos')
    
    def diminuir_claridae(self, qtd_diminui):
        print(f'Diminuindo a claridade em {qtd_diminui} pontos')

monitor = MonitorFullHD()
monitor.aumentar_claridade(5)
monitor.diminuir_claridae(5)
