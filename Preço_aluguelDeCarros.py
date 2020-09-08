dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos KM rodados?'))
d = (dias * 60) + (km * 0.15)
print(' Para {} dias alugados e {} Km rodados, o preço total foi de {:.2f} Reais'.format(dias, km, d))
