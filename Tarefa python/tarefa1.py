def remove_repetidos(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l

lista = [4, 2, 5, 1, 6, 4, 8, 6, 7, 7, 7, 8, 9]

lista = remove_repetidos(lista)
print (lista)