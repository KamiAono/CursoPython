valor1 = float(input('Digite o primeiro valor'))
valor2 = float(input('Digite o segundo valor'))
valor3 = float(input('Digite o terceiro valor'))

if valor1 < valor2 + valor3 and valor2 < valor1 + valor3 and valor3 < valor1 + valor2 :
    print('O valores informados podem formar um triângulo')
    if valor1 == valor2 ==valor3:
        print('O triâgulo formado é um triâgulo equilátero')
    if valor3 != valor2 != valor1 != valor3:
        print('O triângulo formado é escaleno')
    else:
        print('Isoceles')


else:
    print('Os valores informados não formam um triângulo')