import math
co = float(input('digite um numero do cateto oposto'))
ca =float(input('digite o valor do cateto adjacente'))
print('Para {} de cateto oposto e {} de cateto adjacente, o valor da hipotenusa será {:.2f}'.format(co, ca, math.hypot(co,ca)))
