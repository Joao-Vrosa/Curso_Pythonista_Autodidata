import webbrowser # Utilizado para abrir o browser
import threading
import time


def extrair_dados_do_Site(site):
    print(f'Estamos navegando ate o site {site}')
    webbrowser.open_new(site) # Abreindo o site
    for i in range(1, 21):
        print(f'Processando dados - {i}/20')
        time.sleep(1)
    print('Finalizando extracao de dados!')

def baixar_arquivos():
    for i in range(1, 11):
        print(f'Baixando arquivos - {i}/10')
        time.sleep(1)
    print('Arquivos baixados!')


nova_thread = threading.Thread(target=extrair_dados_do_Site, args=('http:www.devaprender.com',), daemon=True)
nova_thread.start() # Inicializar a thread
nova_thread.join() # Finalizar a thread
baixar_arquivos()
