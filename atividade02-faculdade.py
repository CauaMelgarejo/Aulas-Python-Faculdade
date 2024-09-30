#importando o numpy
import numpy as np

#dados dos participantes
participantes = [
    {
        'nome':'Alice',
        'localizacao':'EUA',
        'afiliacao':'Universidade A',
        'interesse':["Engenharia de software", "TI"]
    },
    {
        'nome':'Bob',
        'localizacao':'Alemanha',
        'afiliacao':'Universidade B',
        'interesse':["Engenharia de software", "Matematica"]
    },
    {
        'nome':'Ana',
        'localizacao':'Brasil',
        'afiliacao':'Universidade C',
        'interesse':["Design", "Estetica"]
    }
]

#usando sets para identificar diferentes regiões dos participantes
regioes = set(participante['localizacao'] for participante in participantes)

# Usando um dicionário para categorizar afiliações
afiliacoes = {}
for participante in participantes:
    afiliacao = participante['afiliacao']
    if afiliacao not in afiliacoes:
        afiliacoes[afiliacao] = []
    afiliacoes[afiliacao].append(participante['nome'])

# Usando NumPy para analisar áreas de interesse
areas_de_interesse = np.array([interesse for participante in participantes for interesse in participante['interesse']])
interesses_unicos, contagem = np.unique(areas_de_interesse, return_counts=True)
areas_mais_popular = interesses_unicos[np.argmax(contagem)]

#Resultados
print("Regiões dos participantes:", regioes)
print("Afiliação dos participantes:")
for afiliacao, nomes in afiliacoes.items():
    print(f'{afiliacao}: {", ".join(nomes)}')

print('Área de interesse mais popular:', areas_mais_popular)
