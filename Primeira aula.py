a = int(input('Digite o primeiro valor:'))
b = int(input('Digite o segundo valor:'))
c = int(input('Digite o terceiro valor:'))
if a > b and a > c:
    print('O maior valor é A sendo {}'.format(a))
    d = a-b
    print('E a difernça de A e B é {}'.format(d))
    e = a - c
    print('E a difernça de A e C é {}'.format(e))
elif b > a and b > c:
    print('O maior valor é B sendo {}'.format(b))
    d = b-a
    print('E a difernça de B e A é {}'.format(d))
    e = b-c
    print('E a difernça de B e C é {}'.format(e))
else:
    print('O maior valor é C sendo {}'.format(c))
    d = c-a
    e = c-b
    print('E a difernça de B e A é {}'.format(d))
    print('E a difernça de C e B é {}'.format(e))
print('Fim do programa !')