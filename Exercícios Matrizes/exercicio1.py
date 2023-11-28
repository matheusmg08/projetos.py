"""
1 - Programa que armazena os nomes e idades de 10 pessoas em uma matriz, e imprime o nome da pessoa mais nova
"""
matriz = []
for i in range(10):
    nome = input(f"Digite o nome {i+1}: ")
    idade = int(input(f"Digite a idade {nome}: "))
    matriz.append([nome, idade])
pessoa_jovem = matriz[0]

for pessoa in matriz:
    if pessoa[1] < pessoa_jovem[1]:
        pessoa_jovem = pessoa
print ("-" *80)
print ("Pessoa mais nova:")
print (pessoa_jovem[0]) 