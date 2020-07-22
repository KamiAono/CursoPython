s = float(input('Digite o valor do salário R$'))
print('-=-'*50)
print('Para salário acima de 1250, o aumento será de 10% e para salários no valor igual ou abaixo 1250 o aumento será de 15%')
print('-=-'*50)
if s <= 1250 :
    a1 = (s * 15 / 100) + s
else:
    a1 = (s * 10 / 100) + s
print('Para  um salário minimo no valor de {}R$ o valor do novo salário será  de {}'.format(s, a1))
