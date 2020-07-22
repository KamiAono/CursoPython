from math import radians, sin, cos, tan
an = float(input('Digite um numero para graus'))
s = sin(radians(an))
c = cos(radians(an))
t = tan(radians(an))
print('Para {}° temos {:.2f} de seno, {:.2f} de cosseno e {:.2f} de tangente'.format(an, s, c, t))