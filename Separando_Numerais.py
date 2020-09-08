n = int(input('digite um numero'))
#m = str(n)
#print('analisando o numero{}'.format(n))
#print('Unidade : {}'.format(m[3]))
#print('Dezena: {}'.format(m[2]))
#print('Centena: {}'.format(m[1]))
#print(' Milhar: {} '.format(m[0]))  ( Vamos tentar o metodo 2, pq esse não da pra digitar numeros abaixo de 1000 pois da erro)

u = n // 1 % 10
d = n // 10% 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade: {}'.format(u))
print( 'Dezena : {}'.format(d))
print('Centena: {}'.format(c))
print(' Milhar: {}'.format(m))

