peso = float(input('Digite seu peso '))
altura = float(input('Digite sua altura em metros'))
imc = peso / altura**2
if imc < 18.5:
    print('Seu IMG É {}, Você está abaixo do peso ideal'.format(imc))
elif imc > 18.5 and imc < 25.1 :
    print(' Seu IMC é {}, PARABENS, Você está com o peso ideal!'.format(imc))
elif imc > 25 and imc < 30.1:
    print('Seu IMC é {}, Você está com sobrepeso'.format(imc))
elif imc > 30 and imc < 40.1:
    print('Seu IMC é {}, Você está com Obesidade!'.format(imc))
elif imc > 40:
    print('Seu IMC é {}, Você está com obesidade mórbida, se cuide mais!!'.format(imc))