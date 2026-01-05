# import math

# n = float(input("Informe o teu nome "))
# x = n * math.pi

# print('x = n * pi = ', n)
# print('Teto de x = ', math.ceil(x))
# print('Piso de x = ', math.floor(x))
# print('Log de x na base 10 = ', math.log(x, 10))
# print('Raiz de x = ', math.sqrt(x))


# vamos criar um programa que toma uma decisao usando o if

# nota = float(input('Informe a tua nota \n'))
# if nota >= 60:
#     print('Aprovado')
# print("Boas ferias camarada")

# n = float (input('Inforame a tua nota'))

# if n >= 60 :
#     print('aprovado')
# else:
#     if n >= 40:
#         print('Realiacao')
#     else:
#         print('Reprovado ')
# print('Boas ferias')
# Por baixo teremos uma equacao do segundo grau co desicao 

import math

print('Informe os termos da equacao Ax + Bx + C')

a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))

if a== 0:
    print('Nao e uma equacao de segundo grau')
else:
    delta = b**2 - 4 * a * c
    if delta < 0:
        print('A equacao nao tem raizes ')
    elif (delta == 0):
        x1 = b * (-1) / 2 * a
        print('A equacao possui duas raizes:')
    else:
        raiz_delta = math.sqrt(delta)
        x1 = (b * (-1) + raiz_delta) / 2 * a
        x2 = (b * (-1) - raiz_delta) / 2 * a
        print('x1 = ', x1)
        print('x2 =', x2)
