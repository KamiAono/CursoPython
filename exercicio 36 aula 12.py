valor = float(input('Qual o valor da casa?R$'))
salario = float(input('Qual o seu salário? R$'))
tempo = int(input('Em Quantos anos você pretende pagar?'))
prestacao = valor / (tempo * 12)
print('Para pagar uma casa de {:.2f} R$ em {} anos, a prestação será de {:.2f} R$'.format(valor, tempo, prestacao))
minimo = salario * (30 /100)
if prestacao <= minimo :
    print('O emprestimo pode ser concedido!')
else:
    print(' O emprestimo pode não ser concedido')