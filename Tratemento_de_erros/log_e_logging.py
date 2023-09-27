# Log e Logging( Uma forma de manter um histórico de o que acontece na sua aplicação.

import logging

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a', format='%(levelname)s - %(message)s - %(asctime)s')

try:
    email = input('Digite o seu E-mail: ')
    senha = int(input('Senha: '))

    if senha == 1234:
        print('Login efetuado com sucesso!')
        logging.info(f'{email} entrou em sua conta bancaria!')
except ValueError as erro:
    print('Digit apenas numeros!')
    logging.warning(erro)
    
