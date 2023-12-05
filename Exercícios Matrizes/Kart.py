"""
Uma pista de Kart permite 10 voltas para cada um de 6 corredores. Faça um programa que leia os nomes e os tempos (em segundos) de cada volta de cada corredor e guarde as informações em uma matriz. Ao final, o programa deve informar:
a) De quem foi a melhor volta da prova, e em que volta
b) Classificação final em ordem (1º o campeão)
c) Qual foi a volta com a média mais rápida
"""
n_corredores = 6
n_voltas = 10
print ("Nome e tempo de pilotos")
print("=" *50)

tempos = [[0] * n_voltas for _ in range(n_corredores)]
for i in range(n_corredores):
    nome_piloto = input(f"Digite o nome do piloto {i + 1}: ")
    for j in range(n_voltas):
        tempo_volta = float(input(f"Digite o tempo da volta {j + 1} para {nome_piloto} em segundos: "))
        tempos[i][j] = tempo_volta
print ("=" *50)
print ("a) -->  Econtrando a melhor volta:")
melhor_volta_tempo = tempos[0][0]
melhor_volta_piloto = 1
melhor_voltas = 1

for i in range(n_corredores):
    for j in range(n_voltas):
        if tempos[i][j] < melhor_volta_tempo:
            melhor_volta_tempo = tempos[i][j]
            melhor_volta_piloto = i + 1
            melhor_voltas = j + 1
print(f"A melhor volta da prova foi do piloto {melhor_volta_piloto} na volta {melhor_voltas} com o tempo de {melhor_volta_tempo} segundos.")
print ("=" *50)
print ("b) -->  Classificação em ordem (1º o campeão):")
classificacao_final = list(range(n_corredores))
for i in range (n_corredores):
    for j in range (i + 1, n_corredores):
        if sum(tempos[i]) > sum(tempos[j]):
                        classificacao_final[i], classificacao_final[j] = classificacao_final[j], classificacao_final[i]
for posicao, corredor in enumerate(classificacao_final, start=1):
    print(f"{posicao}º lugar: Piloto {corredor + 1} - Tempo total: {sum(tempos[corredor])} segundos")
print ("=" *50)
print ("c) -->  Qual foi a volta com a média mais rápida:")
media_por_volta = [sum(tempos[i][j] for i in range(n_corredores)) / n_corredores for j in range(n_voltas)]
volta_media_rapida = media_por_volta.index(min(media_por_volta)) + 1
print(f"A volta com a média mais rápida foi a volta {volta_media_rapida}.")






