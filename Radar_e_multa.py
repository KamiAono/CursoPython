v = float(input('Digite a velocidade do carro'))
t = (v - 80) * 7
if v <= 80:
    print('Parabéns, sua velocidade está dentro do limite máximo permitido')
else:
    print('Você excedeu a velocidade de 80Km/h e irá ser MULTADO em {} R$'.format(t))
