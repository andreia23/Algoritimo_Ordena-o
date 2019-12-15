from time import perf_counter

#----------------------------- BoubleSort -----------------------------#

def boubblesort(lista):
    #cronometro do boubblesort
    inicio = perf_counter()

    #busca
    list_size = len(lista)
    print('list_size: ',list_size)
    for i in range(list_size - 1):
        print('i: ',i)
        for j in range(list_size - 1):
            print('j: ',j)
            #troca de elemento caso o próximo elemento seja maior
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                print('lista[j], lista[j + 1]: ',lista[j], lista[j + 1])
    
    fim = perf_counter() - inicio
    return lista, fim



lista = [2,8,5,3,1]
print(boubblesort(lista))
