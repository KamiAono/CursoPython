from datetime import date
nasc = int(input('Ano de nascimento: '))
anos = date.today().year - nasc
print('O atleta tem {} anos.'.format(anos))
if anos > 0 and anos <= 9:
    print('Classificação: MIRIM')
elif anos > 9 and anos <= 14:
    print('Classificação: INFANTIL')
elif anos > 14 and anos <= 19:
    print('Classificação: JUNIOR')
elif anos > 19 and anos <= 25:
    print('Classificação: SÊNIOR')
elif anos > 25:
    print('Classificação: MASTER')
