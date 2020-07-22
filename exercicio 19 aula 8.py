from random import choice
n1 = str(input('Digite um nome'))
n2 = str(input(' Digite outro nome'))
n3 = str(input('Digite outro nome'))
n4 = str(input('Digite outro nome'))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

#Posso tentar fazer um jogo de tabuleiro com dados ?