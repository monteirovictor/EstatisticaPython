import pandas as pd
import numpy as np
import random

df=pd.read_csv("C:/Users/Gabriel/Desktop/EstatisticaPython/census.csv")
df.head()

df.tail()

"""## amostra simples

"""

df_amostra_simples=df.sample(n=100)
df_amostra_simples

"""##função amostra simples"""

from pandas.core.common import random_state
def funcao_amostra_simples(df,amostras):
  return df.sample(n=amostras,random_state=1)

df_amostra_simples_funcao=funcao_amostra_simples(df,100)
df_amostra_simples_funcao

"""## Amostra sistemática"""

df.shape

len(df)//100

random.seed(1)
random.randint(0,85)

17+85

102+85

np.arange(17,len(df),step=85)

"""##Função Sistemática"""

def amostra_sitematica(df,amostras):
  intervalo=len(df)//amostras
  random.seed(1)
  inicio=random.randint(0,intervalo)
  indices=np.arange(inicio,len(df),step=intervalo)
  amostra_sitematica=df.iloc[indices]
  return amostra_sitematica

df_amostra_sistematica=amostra_sitematica(df,100)

df_amostra_sistematica.shape

"""##Amostragem por Grupos """

len(df)//10

from numpy.ma.core import append
grupos=[]
id_grupo=0
contagem=0
for _ in df.iterrows():
  grupos.append(id_grupo)
  contagem+=1

  if contagem>853:
    contagem=0
    id_grupo+=1

print(grupos)

np.unique(grupos,return_counts=True)

np.shape(grupos),df.shape

df['grupo']=grupos

df.head()

df.head()

random.randint(0,9)

df_agrupamento=df[df['grupo']==9]

df_agrupamento.shape

df_agrupamento['grupo'].value_counts()

"""##Função Amostragem Grupos"""

def amostragem_grupos(df,numero_grupos):
  intervalo = len(df)/numero_grupos
  
  grupos=[]
  id_grupo=0
  contagem=0
  for _ in df.iterrows():
    grupos.append(id_grupo)
    contagem+=1

  if contagem>intervalo:
    contagem=0
    id_grupo+=1

  df['grupo']=grupos
  grupo_selecionado=random.randint(0,numero_grupos)
  return df[df['grupo']==grupo_selecionado]

df_agrupamento=amostragem_grupos(df,100)
df_agrupamento.shape,df_agrupamento['grupo'].value_counts()

"""##Amostragem Estratificada """

from sklearn.model_selection import StratifiedShuffleSplit

df['income'].value_counts()

2034/len(df),6495/len(df)

0.2384525205158265+0.761430246189918

100/len(df)

split=StratifiedShuffleSplit(test_size=0.0030711587481956942)

for x, y in split.split(df,df['income']):
  df_x=df.iloc[x]
  df_y=df.iloc[y]

df_x.shape,df_y.shape

df.head()

df_y['income'].value_counts()