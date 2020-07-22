d = float(input('Digite a distância da viagem? Km'))
if d <= 200:
    p1 = (d * 0.5)
    print('Viajando a  {} Km, o preço pago será de {} R$'.format(d, p1))
else:
    p2 = d * 0.45
    print('A {} Km o preço a se pagar será de {} R$'.format(d, p2))

#segundo modo é
# preço = d * 0.50 if d <= 200 else d * 0.45