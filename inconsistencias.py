import pandas as pd
import numpy as np

pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('clientes_remove_outliers.csv')

print(df.head())

# Mascarar dados pessoais 
df['cpf_mascara'] = df['cpf'].apply(lambda cpf: f'{cpf[:3]}.***.***-{cpf[-2:]}')

# Corrigir datas 
df['data'] = pd.to_datetime(df['data'], format='%Y-%m-%d', errors='coerce')

data_atual = pd.to_datetime('today')
df['data_atualizada'] = df['data'].where(df['data'] <= data_atual, pd.to_datetime('1900-01-01')) 
