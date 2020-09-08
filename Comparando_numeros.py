n1 = int(input('Digite um número inteiro'))
n2 = int(input('Digite outro número inteiro'))

if n1 > n2:
    print('O maior número é o numero {}'.format(n1))
elif n2 > n1:
    print(' O maior número é o {}'.format(n2))
elif n1 == n2:
    print('Os dois números são iguais')
