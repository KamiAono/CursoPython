nota1 = float(input('Digite a primeira nota'))
nota2 = float(input('Digite a segunda nota'))
m = (nota1 + nota2) /2
print('Sua média foi de {:.1f}'.format(m))
#if m >= 6:
 #   print('Parabéns, continue assim!')
#else:
#    print('Sua nota ficou abaixo da média, estude mais!')
print('Parabens'if m >= 6 else 'Estude mais') #(condição simplificada)
