a = int(input( 'Digite um numero'))
b = int(input('Digite o segundo numero'))
c = int(input('Digite o terceiro numero'))
#verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor digitado foi {}'.format(menor))
#Verificando quem é o maior
maior = a
if b > a and b > c :
    maior = b
if c > a and c > b :
    maior = c
print('O maior valor digitado foi {}'.format(maior))
