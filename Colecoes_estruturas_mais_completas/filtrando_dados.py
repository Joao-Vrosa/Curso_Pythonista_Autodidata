nomes = ['Joao', 'Emilly', 'Gaba', 'Lena']

def pessoa_aprovada(pessoa):
    if pessoa == 'Joao':
        return True
    else:
        return False
    

print(list(filter(pessoa_aprovada, nomes)))
print(list(map(pessoa_aprovada, nomes)))
