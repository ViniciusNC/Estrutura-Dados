comps = trocas = passd = 0

def selection_sort(lista):

    global comps, trocas, passd
    comps = trocas = passd = 0

    for pos_sel in range(len(lista) - 1):

        passd += 1

        pos_menor = pos_sel + 1

        for pos in range(pos_menor + 1, len(lista)):
            
            comps += 1
            if lista[pos] < lista[pos_menor]: pos_menor = pos

        comps += 1
        if lista[pos_menor] < lista[pos_sel]:
            lista[pos_menor], lista[pos_sel] = lista[pos_sel], lista[pos_menor]
            trocas += 1

import sys, tracemalloc
sys.dont_write_bytecode = True
from time import time


from data.emp10mil import empresas

tracemalloc.start()
hora_ini = time()
selection_sort(empresas)
hora_fim = time()

mem_atual, mem_pico = tracemalloc.get_traced_memory()
tracemalloc.stop()          # Termina a medição de memória


print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
print(f"Passadas: {passd}; comparações: {comps}; trocas: {trocas}")
print(f"Pico de memória: { mem_pico / 1024 / 1024 }MB")