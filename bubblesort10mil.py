# Variáveis de contagem
comps = trocas = passd = 0

def bubble_sort(lista):

    global comps, trocas, passd
    comps = trocas = passd = 0

    while True:

        passd += 1

        trocou = False

        for pos in range(len(lista) - passd):

            if lista[pos + 1] < lista[pos]:

                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]
                trocas += 1
                trocou = True 

            comps += 1

        if not trocou:
            break

import sys, tracemalloc

sys.dont_write_bytecode = True 

from time import time
from data.emp10mil import empresas

tracemalloc.start()         # Inicia medição do consumo de memória
hora_ini = time()
bubble_sort(empresas)
hora_fim = time()


mem_atual, mem_pico = tracemalloc.get_traced_memory()
tracemalloc.stop()          # Termina a medição de memória


print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
print(f"Passadas: {passd}; comparações: {comps}; trocas: {trocas}")
print(f"Pico de memória: { mem_pico / 1024 / 1024 }MB")

