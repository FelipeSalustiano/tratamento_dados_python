import pandas as pd
from scipy import stats

pd.set_option('display.width', None)

df = pd.read_csv('clientes_limpeza.csv')

df_filtro_basico = df[df['idade'] > 100]

print('Filtro básico: \n', df_filtro_basico[['nome', 'idade']].to_string(index=False))

# Identificador outliers com Z-score 
z_score = stats.zscore(df['idade'].dropna())
outliers_z = df[z_score >= 3]
print('Vizualizando outliers através do Z-score: \n', outliers_z)
# OBS.: Outliers significa valores atípicos, ou seja, dados fora da norma. Z-score significa o cáculo de descio padrão

# Filtrar outliers com Z-score
df_zscore = df[(stats.zscore(df['idade']) < 3)]

# Identificar outliers com IQR
