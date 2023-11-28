"""
2- Faça um programa que leia uma matriz 3x3 e multiplique os elementos da diagonal principal da matriz por um
número k. Imprima a matriz na tela antes e depois da multiplicação.
"""
k = 5
import random
matriz = []
n = 3
m = 3
pares = 0
for li in range(n):
    colunas = []
    for col in range(m):
        sorteado = random.randint(1,30)
        colunas.append(sorteado)
    matriz.append(colunas)
for linha in range(n):
    for coluna in range(m):
        print(matriz[linha][coluna], end='\t')
    print()
print("=" *70)
k = int(input("Digite o valor de K: "))
for i in range (3):
    matriz[i][i] *= k
print("=" *70)
print("Matriz com a diagonal multiplicada")
#multiplicando a matriz diagonal pelo valor de k
for linha in matriz:
    for multi in linha:
        print(multi, end='\t')
    print()




