nome = input('Digite seu nome completo: ')
nl = nome.upper().strip()
res = 'CRUZ' in nl
print('\nVocê possui "Cruz" no nome? True significa Sim e False significa Não.\nResposta: {}'.format(res))
