import pandas as pd

df = pd.read_csv('clientes.csv')

pd.set_option('display.width', None)
print('Dados brutos: \n', df.head())

# -=-=-= Remover dados =-=-=- 
df.drop('pais', axis=1, inplace=True) # axis=1 == Coluna 
df.drop(2, axis=0, inplace=True) # axis=0 == Linha 
# Explicando inplace=True: é usado para realizar modificações diretamente no objeto original, sem criar uma cópia modificada.

# -=-=-= Normalizar dados =-=-=-
df['nome'] = df['nome'].str.title() 
df['endereco'] = df['endereco'].str.lower() 
df['estado'] = df['estado'].str.upper()

# -=-=-= Converter tipos de dados =-=-=- 
df['idade'] = df['idade'].astype(int) # astype(int) converte os dados para inteiro

print('Normalizar textos: \n', df.head())

# -=-=-= Tratar valores nulos =-=-= 
df_fillna = df.fillna(0) # Substitui valores nulos por 0 
df_dropna = df.dropna() # Remove registros com valores nulos 
df_dropna4 = df.dropna(thresh=4) # Mantem registros com no mínimo 4 valores não nulos 
df = df.dropna(subset=['cpf']) # Remove registro com CPF nulos 

df['endereco'] = df['endereco'].fillna('Endereço não informado') # Muda os dados da coluna endereco se for nulo
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean())

# -=-=-= Tratar formato de dados =-=-=- 
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

# -=-=-= Tratar valores duplicados =-=-=-
print('Qtd registros atual: ', df.shape[0])
df.drop_duplicates()
df.drop_duplicates(subset='cpf', inplace=True)
print('Qtd de linhas com registros duplicados removidos: ', len(df))
# OBS.: usar o len(df) e o df.shape[0] retornariam a mesma resposta nesse caso

print('Dados limpos: \n', df.head())

# Salvando dataframe 
df['data'] = df['data_corrigida']
df['idade'] = df['idade_corrigida']

df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', ]]
df_salvar.to_csv('clientes_limpeza.csv', index=False)

print('Novo dataframe: \n', pd.read_csv('clientes_limpeza.csv').head())
