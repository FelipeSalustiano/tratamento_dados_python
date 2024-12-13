import pandas as pd

df = pd.read_csv('clientes.csv')

pd.set_option('display.width', None)
print(df.head())

# Remover dados 
df.drop('pais', axis=1, inplace=True) # axis=1 == Coluna 
df.drop(2, axis=0, inplace=True) # axis=0 == Linha 

# Normalizar dados 
df['nome'] = df['nome'].str.title() 
df['endereco'] = df['endereco'].str.lower() 
df['estado'] = df['estado'].str.upper()

# Converter tipos de dados 
df['idade'] = df['idade'].astype(int) # astype(int) converte os dados para inteiro

print('Normalizar texos ', df.head())

# Tratar valores nulos 
df_fillna = df.fillna(0) # Substitui valores nulos por 0 
df_dropna = df.dropna() # Remove registros com valores nulos 
df_dropna4 = df.dropna(thresh=4) # Mantem registros com no mínimo 4 valores não nulos 
df = df.dropna(subset=['cpf']) # remove registro com CPF nulos 

df['endereco'] = df['endereco'].fillna('Endereço não informado') # Muda os dados da coluna endereco se for nulo
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean())
 