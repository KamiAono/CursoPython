r = float(input('Digite o primeiro numero'))
r2 = float(input('Digite o segundo numro'))
r3 = float(input('Digite o terceiro numero'))
if r < r2 + r3 and r2 < r + r3 and r3 < r + r2 :
    print(' Os valores acima podem formar triângulos')
else:
    print('Os valores acima não formam triângulo')
