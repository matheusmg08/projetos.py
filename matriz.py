#Adicione elementos de forma aleatória em uma matriz NXM e retorne e quantidade de numeros pares!
import random
matriz = []
n = 4
m = 5
pares = 0
for li in range(n):
    colunas = []
    for col in range(m):
        sorteado = random.randint(1,100)
        colunas.append(sorteado)
        if (sorteado % 2) == 0:
            pares += 1
    matriz.append(colunas)
for linha in range(n):
    for coluna in range(m):
        print(matriz[linha][coluna], end='\t')
    print()
print("=" *50)
print(f"A quantidade de números pares na matriz é: {pares}")