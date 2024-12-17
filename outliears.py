import pandas as pd
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('clientes_limpeza.csv')

df_filtro_basico = df[df['idade'] > 100]

print('Filtro básico: \n', df_filtro_basico[['nome', 'idade']].to_string(index=False))

# Identificando outliers com Z-score 
z_score = stats.zscore(df['idade'].dropna())
outliers_z = df[z_score > 3]
print('Vizualizando outliers através do Z-score: \n', outliers_z)
# OBS.: Outliers significa valores atípicos, ou seja, dados fora da norma. Z-score significa o cáculo de descio padrão

# Filtrar outliers com Z-score
df_zscore = df[stats.zscore(df['idade']) < 3]

# Identificar outliers com IQR
Q1 = df['idade'].quantile(0.25)
Q3 = df['idade'].quantile(0.75)
IQR = Q3 - Q1

limite_baixo = Q1 - 1.5 * IQR
limite_alto = Q3 + 1.5 * IQR

print(f'''Limite IQR: 
limite_alto: {limite_alto}
limite_baixo: {limite_baixo}
''')

outliers_iqr = df[(df['idade'] < limite_baixo) | (df['idade'] > limite_alto)]
print('Outiliers pelo IQR: \n', outliers_iqr)

# Filtrar outliers com IQR
df_iqr = df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

limite_baixo = 1
limite_alto = 100
df[(df['idade'] >= limite_baixo) & (df['idade'] <= limite_alto)]

# Filtrar endereços invalidos 
df['endereco'] = df['endereco'].apply(lambda x: 'Endereco invalido' if len(x.split('\n')) < 3 else x)
print('Qtd registros com enderecos grandes: \n', (df['endereco'] == 'endereco invalido').sum())

# Tratar campos de texto 
df['nome'] = df['nome'].apply(lambda x: 'Nome invalido' if isinstance(x, str) and len(x) > 50 else x)
print('Qtd registros com nomes grandes: \n', (df['nome'] == 'Nome invalido').sum())
# OBS.: isinstance(x, str) verifica se o valor de é string. É bem importante usar esse conceito, pois isso garante que o código só se aplica a valores que são strings. 

print('Dados com Outliers tratados: \n', df)

df.to_csv('clientes_remove_outliers.csv', index=False)
