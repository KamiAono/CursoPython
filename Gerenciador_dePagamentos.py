print('{:=^50}'.format('Aono informática'))
valor = float(input('Digite o valor das compras? R$'))
print('''FORMA DE PAGAMENTO
[ 1 ] á Vista dinheiro/cheque com 10% de desconto
[ 2 ] 2x no cartão
[ 3 ] 3x ou mais no cartão com 20% de juros''')
aperte = int(input('Digite a opção desejada'))
print('-=-'*20)
print('Valor a pagar:')
if aperte == 1:
    total = valor - (valor * 10 / 100)
    print('Total a pagar é {} R$'.format(total))
elif aperte == 2:
    total = valor / 2
    print('Você irá pagar em 2 vezes de  {} R$'.format(total))
elif aperte == 3:
    total = (valor + (valor * 20/100)) / 3
    print('Você irá pagar {} R$ em 3 prestações '.format(total))
else:
    print('Opção inválida, tente novamente!')
print('-=-'*20)
print('Muito obrigado pela preferência, tenha um bom dia!')
print('-=-'*20)
