from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções :
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA ''')
escolha = int(input('Qual a sua escolha?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!')

print('-=-'*15)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[escolha]))
print('-=-'*15)
if computador == 0:
    if escolha == 0:
        print('Empatou!')
    if escolha == 1:
        print('Você perdeu!')
    elif escolha == 2:
        print('Parabéns! Você ganhou!')
    elif escolha >= 3:
        print('Jogada Inválida')
if computador == 1:
    if escolha == 0:
        print('Você perdeu!')
    if escolha == 1:
        print('Empatou!!')
    elif escolha == 2:
        print('Parabéns! Você ganhou!')
    elif escolha >= 3:
        print('Jogada Inválida')
if computador == 2:
    if escolha == 0:
        print('Parabéns! Você ganhou!!')
    if escolha == 1:
        print('Você perdeu!')
    elif escolha == 2:
        print('Empatou!')
    elif escolha >= 3:
        print('Jogada Inválida')

