catalogo = 'Lapís', 1.70, 'Borracha', 3.00, 'Apagador', 90.00, 'giz', 80.00, 'mochila', 123.00, 'cartaz', 230.00
for i in catalogo:
    if type(i) == str:
        print(i, '.'*20, end='')
    else:
        print(f'R$ {i:.2f}')

