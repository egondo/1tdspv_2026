#criando uma matriz 3x3
tab = []
for i in range(3):
    tab.append([' '] * 3)

tab[0][0] = 'X'
tab[1][1] = 'O'
tab[2][2] = 'X'

#imprimindo a matriz
print('')
print('')
for lin in tab:
    print(lin)