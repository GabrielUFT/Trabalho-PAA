import math
import random
import copy

for i in [1000,10000,100000,1000000]:
    data_crescente = [q for q in range(0,i)]
    data_decrescente = [q for q in range(i, 0, -1)]
    data_aleatorio = copy.deepcopy(data_decrescente)
    [random.shuffle(data_aleatorio)]

    rcresc = open(f'arquivos/{i}-cresc.txt',"w")
    for n in data_crescente:
        rcresc.write(f'{n}\n')
    rcresc.close()

    rdecresc = open(f'arquivos/{i}-decresc.txt',"w")
    for n in data_decrescente:
        rdecresc.write(f'{n}\n')
    rdecresc.close()

    ralea = open(f'arquivos/{i}-aleat.txt',"w")
    for n in data_aleatorio:
        ralea.write(f'{n}\n')
    ralea.close()