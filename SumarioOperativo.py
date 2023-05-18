import re
import os
import shutil
import pandas as pd
from datetime import datetime as dt
from time import sleep
import io
import matplotlib.pyplot as plt

'''Ler PDO_Sumoper'''
'''Encontrar uma pasta dentro de um diretório e extrair os dados'''
for diretorio, subpastas, arquivos in os.walk(os.path.dirname(os.path.abspath(__file__))):
    for arquivo in arquivos:
        # print(arquivos)
        if arquivo.startswith('PDO_SUMAOPER.DAT'):
            print(os.path.join(diretorio, arquivo))
            file=os.path.join(diretorio, arquivo)
            print(file[90:96])
            print(file[109:111])
''' Abrir arquivo em modo leitura'''
with open(file, "r") as f:
    # Ler linhas específicas do arquivo
    linhas = f.readlines()[363:530]
'''Geraçaõ hidroeletrica Bloco 3 -Dessem - PDOSumaope'''
[vt, usina, prod, energia, vz_t, gh]=list(),list(),list(), list(), list(), list()
for i in range(1,165):
    vt.append(linhas[i+2][66:72])
    usina.append(linhas[i+2][5:18])
    prod.append(linhas[i+2][77:81])
    vz_t.append(linhas[i+2][25:33])
    gh.append(linhas[i + 2][34:43])
    i+=1
lista_de_tuplas = list(zip(usina, vt, prod, vz_t, gh))
df = pd.DataFrame(lista_de_tuplas, columns=['Usina', 'Vazão Não-Turbinada', 'prod', 'Vazão Turbinada', 'Geração Hidráulica'])
df['Vazão Não-Turbinada']=df['Vazão Não-Turbinada'].replace("  -   ", 0.00)
df['Vazão Não-Turbinada']=pd.to_numeric(df['Vazão Não-Turbinada'])
df['Vazão Turbinada']=df['Vazão Turbinada'].replace("   -    ", 0.00)
df['Vazão Turbinada']=pd.to_numeric(df['Vazão Turbinada'])
df['Geração Hidráulica']=df['Geração Hidráulica'].replace("    -    ", 0.00)
df['Geração Hidráulica']=pd.to_numeric(df['Geração Hidráulica'])
df['prod']=df['prod'].replace( ' -  ', 0.00)
df['prod']=pd.to_numeric(df['prod'])
df['ENERGIA VERTIDA']=df['Vazão Não-Turbinada']*df['prod']
df['ENERGIA_ACUM'] = df['ENERGIA VERTIDA'].cumsum()
soma = df['ENERGIA VERTIDA'].sum()
# print(soma)
print(df.info())
print(df['Usina'])



'''Gráficos'''
# Plotar o gráfico de barras
# df = df.sort_values(by='ENERGIA VERTIDA', ascending=False)
# plt.figure(figsize=(12,6))
# plt.bar(df['Usina'], df['ENERGIA VERTIDA'])
# plt.xticks(rotation=90)
# plt.xlabel('Usinas')
# plt.ylabel('Energia Vertida (MWh)')
# plt.title('Energia Vertida por Usina')
# plt.show()

# df = df.sort_values(by='ENERGIA_ACUM', ascending=False)
# plt.figure(figsize=(12,6))
# plt.bar(df['Usina'], df['ENERGIA_ACUM'])
# plt.xticks(rotation=90)
# plt.xlabel('Usinas')
# plt.ylabel('Energia Vertida (MWh)')
# plt.title('Energia Vertida por Usina')
# plt.show()

# Plotar o gráfico de barras
# df = df.sort_values(by='Vazão Turbinada', ascending=False)
# plt.figure(figsize=(12,6))
# plt.bar(df['Usina'], df['Vazão Turbinada'])
# plt.xticks(rotation=90)
# plt.xlabel('Usinas')
# plt.ylabel('Vazão Turbinada (m³/s)')
# plt.title('Vazão Turbinada por Usina')

# '''Geração Hidroelétrica - DESSEM'''
# df = df.sort_values(by='Geração Hidráulica', ascending=False)
# plt.figure(figsize=(12,6))
# plt.bar(df['Usina'], df['Geração Hidráulica'])
# plt.xticks(rotation=90)
# plt.xlabel('Usinas')
# plt.ylabel('Geração Hidráulica (MWmed)')
# plt.title('Geração Hidráulica por Usina')
# plt.show()
