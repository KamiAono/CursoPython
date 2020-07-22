media1 = float(input('Escreva a primeira nota'))
media2 = float(input('Escreva a segunda nota'))
mediaf = (media1 + media2) / 2
if mediaf < 5:
    print('Sua média foi {}, você está reprovado(a)!'.format(mediaf))
elif mediaf > 5 and mediaf < 7:
    print('Sua média foi de {}, você está de recuperação'.format(mediaf))
elif mediaf > 7:
    print('Parabéns! sua média foi de {}, você está aprovado(a)'.format(mediaf))