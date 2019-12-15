
from time import perf_counter

#lista = [2,8,5,3,1]


#------------- Merge --------------#
def merge(left,right):
	result = []
	print('vetor result: ',result)
	i,j = 0, 0
	while i<len(left) and j< len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1
	print('result: ',result)
        
	result += left[i:]
	print('1° result: ',result)
	result += right[j:]
	print('2° result: ',result)
	return result

#----------- Mergesort ------------#
def mergesort_no_crono(lst):
	if(len(lst) <= 1):
		return lst
	mid = int(len(lst)/2)
	print('mid: ',mid)
	left = mergesort_no_crono(lst[:mid])
	print('left: ',left)
	right = mergesort_no_crono(lst[mid:])
	print('right: ',right )
	return merge(left,right)

#---- Cronometro do Mergesort -----#
def mergesort(lista):
    inicio = inicio = perf_counter()
    print(inicio)
    lista_sorteada = mergesort_no_crono(lista)
    fim = perf_counter() - inicio
    return lista_sorteada, fim


lista = [2,8,5,3,1]
print(mergesort(lista))
