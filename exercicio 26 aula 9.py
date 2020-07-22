n = str(input('Digite uma frase')).upper()
print(' A letra A aparece {} vezes na frase'.format(n.count('A')))
print('A letra A aparece na posição {} a primeira vez'.format(n.find('A')))
print('A letra A aparece na posição {} a última vez'.format(n.rfind('A')))