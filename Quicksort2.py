# Implementação do Quick sort
import time
import random
import copy

# Função para encontrar o local da partição

def partition(array, low, high):
    global comparate
    global swap
 
    # Escolhe o elemento mais a direita como pivô
    pivot = array[high]
 
    # Aponta o maior elemento
    i = low - 1
 
    # Percorre todos os elementos
    # Compara cada elemento com o pivô
    for j in range(low, high):
        comparate = comparate + 1
        if array[j] <= pivot:
            swap = swap + 1
 
            # Se um elemento menor que o pivô for encontrado
            # Troca ele com o maior elemento apontado por i
            i = i + 1
 
            # Troca o elemento i pelo elemento j
            (array[i], array[j]) = (array[j], array[i])
 
    # Troca o pivô com o maior elemento apontado por i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Retorna a posição onde a partição finalizou
    return i + 1
# Função para executar o QuickSort

def quickSort(array, low, high):
	if low < high:

		#Encontre o elemento pivô tal que
        # elemento menor que pivô está à esquerda
        # elemento maior que pivô está à direita
		pi = partition(array, low, high)

		# Chamada recursiva para a esquerda do pivô
		quickSort(array, low, pi - 1)

		# Chamada recursiva para a direita do pivô
		quickSort(array, pi + 1, high)

import time

qt = 1000
open('arquivos/relatorioQuickSort.txt','w')
while qt <= 1000000:

    # Convert into a list of list
    lista = [int(a) for a in open(f'arquivos/{qt}-cresc.txt').read().split('\n') if a != '']

    inicio = time.time()
    swap = 0
    comparate = 0

    size = len(lista)

    quickSort(lista,0, size -1)
    tempo = round((time.time() - inicio), 3)
    open(f'arquivos/relatorioQuickSort.txt','a').write(f"{qt} valores: Tempo= {tempo} Trocas= {swap} Comparacoes= {comparate}\n")
    qt *= 10
close('arquivos/relatorioQuickSort.txt')