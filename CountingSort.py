# Implementação do Counting Sort


def countingSort(array):
    size = len(array)
    output = [0] * size
    global increment
    global comparate

    # Inicializa o array de contagem
    maior = 0
    for i in range(0,size):
        if array[i] > maior:
            comparate += 1
            maior = array[i]

    count = [0] * (maior+1)

    # Incrementa um contador para cada elemento no array de contagem
    for i in range(0, size):
        count[array[i]] += 1
        increment += 1


    # Armazena o contador acumulado
    for i in range(1, maior+1):
        count[i] += count[i - 1]
        increment += 1

    # Encontra o índice de cada elemento do array original no array de contagem
    # Coloca os elementos no array de saída
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
        increment += 1

    # Copia os elementos ordenados no array original
    for i in range(0, size):
        array[i] = output[i]

    return output


import time

qt = 1000
open('arquivos/CountingCresc.txt','w')
open('arquivos/CountingDecresc.txt','w')
open('arquivos/CountingAleat.txt','w')
while qt <= 1000000:

    # Relatorio Crescente
    data_cresc = [int(a) for a in open(f'arquivos/{qt}-cresc.txt').read().split('\n') if a != '']
 
    inicio = time.time()
    increment = 0
    comparate = 0

    size = len(data_cresc)

    countingSort(data_cresc)
    tempo = round((time.time() - inicio), 3)
    open(f'arquivos/CountingCresc.txt','a').write(f"{qt} valores: Tempo= {tempo} Incrementacoes= {increment} Comparacoes= {comparate}\n")

    # Relatorio Decrescente
    data_decresc = [int(a) for a in open(f'arquivos/{qt}-decresc.txt').read().split('\n') if a != '']
 
    inicio = time.time()
    increment = 0
    comparate = 0

    size = len(data_decresc)

    countingSort(data_decresc)
    tempo = round((time.time() - inicio), 3)
    open(f'arquivos/CountingDecresc.txt','a').write(f"{qt} valores: Tempo= {tempo} Incrementacoes= {increment} Comparacoes= {comparate}\n")

    # Relatorio Aleatorio
    data_aleat = [int(a) for a in open(f'arquivos/{qt}-aleat.txt').read().split('\n') if a != '']
 
    inicio = time.time()
    increment = 0
    comparate = 0

    size = len(data_aleat)

    countingSort(data_aleat)
    tempo = round((time.time() - inicio), 3)
    open(f'arquivos/CountingAleat.txt','a').write(f"{qt} valores: Tempo= {tempo} Incrementacoes= {increment} Comparacoes= {comparate}\n")
    qt *= 10




