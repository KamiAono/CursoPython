from datetime import date
atual = date.today().year
ano = int(input('Qual ano você nasceu?'))
idade = atual - ano

print('Quem nasceu em {} tem {} anos '.format(ano, idade))
if idade == 18:
    print('Esse é o ano do seu alistamento militar')
elif idade < 18 :
    print('Você ainda não tem 18 anos para se alistar')

elif idade > 18 :
    print('Você já passou da dos 18, se apresente imediatamente!')
   
