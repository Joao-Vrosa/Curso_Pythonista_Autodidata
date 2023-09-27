# idade = 21
# possui_convite = False

# print(idade >= 21 and possui_convite == True)
# print(idade >= 21 or possui_convite == True)

possui_passaporte = False
passagem_comprada = False
menor_de_idade = False


# Uma pessoa só pode viajar se possuir passaporte e tiver a passagem comprada e não for menor de idade
print((possui_passaporte and passagem_comprada) and not menor_de_idade)

# Uma pessoa só pode viajar se possuir passaporte ou tiver a passagem comprada e não for menor de idade
print((possui_passaporte or passagem_comprada) and not menor_de_idade)

# Uma pessoa só pode viajar se não possuir passaporte ou tiver a passagem comprada e não for menor de idade
print((not possui_passaporte or passagem_comprada) and not menor_de_idade)

# Uma pessoa não pode viajar se não possuir passaporte ou não tiver a passagem comprada e for menor de idade
print((not possui_passaporte or not passagem_comprada) and menor_de_idade)
