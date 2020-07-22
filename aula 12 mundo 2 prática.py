nome = str(input('Qual o seu nome?')).upper().strip()
if nome == 'RAI':
    print ('\033[31mVocê é muito lindo!')
elif nome == 'PEDRO' or nome == 'MARIA' or nome == 'LUCAS' or nome == 'JOÃO':
    print('Seu nome é bm popular no Brasil!')
elif nome in 'LUANA, KIANA, YUUKA, PATRICIA':
    print('Belo nome')
else:
    print('Você é muito normal! Eca')
print('Bom dia {}'.format(nome))
#Isso é uma estrutura condicional aninhada, uma estrutura dentro da outra