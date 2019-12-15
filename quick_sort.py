from time import perf_counter

#------------ QuickSort -----------#
def quicksort_no_crono(lista):
    if len(lista) == 1 or len(lista) == 0:
        return lista
    else:
        pivot = lista[0]
        print('pivot: ',pivot)
        i = 0
        for j in range(len(lista)-1):
            if lista[j+1] < pivot:
                lista[j+1],lista[i+1] = lista[i+1], lista[j+1]
                print('lista[j+1],lista[i+1]: ',lista[j+1],lista[i+1])
                print('1° lista: ',lista)
                i += 1
        lista[0],lista[i] = lista[i],lista[0]
        print('lista[0],lista[i]: ',lista[0],lista[i])
        print('2° lista: ',lista)
        bloco_um = quicksort_no_crono(lista[:i])
        print('bloco_um: ',bloco_um)
        bloco_dois = quicksort_no_crono(lista[i+1:])
        print('bloco_dois: ',bloco_dois)
        bloco_um.append(lista[i])
        return bloco_um + bloco_dois

#---- cronometro do quicksort -----#
def quicksort(lista):
    inicio = inicio = perf_counter()
    print('inicio: ',inicio)
    lista_sorteada = quicksort_no_crono(lista)
    fim = perf_counter() - inicio
    return lista_sorteada, fim


lista = [2,8,5,3,1]
print(quicksort(lista))
