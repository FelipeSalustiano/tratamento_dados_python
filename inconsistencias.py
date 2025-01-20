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

df['data_atualizada'] = df['data'].where(df['data'] <= data_atual, pd.to_datetime('1900-01-01')) # Atualiza a coluna 'data_atualizada', mantendo as datas originais se forem menores ou iguais à data atual. Caso contrário, substitui por '1900-01-01'.
df['data_ajustada'] = data_atual.year - df['data_atualizada'].dt.year # Calcula a diferença de anos entre a data atual e a coluna 'data_atualizada' para criar uma coluna inicial de ajuste de idade.
df['data_ajustada'] -= ((data_atual.month <= df['data_atualizada'].dt.month) & (data_atual.day < df['data_atualizada'].dt.day)).astype(int) # Subtrai 1 de 'data_ajustada' se o mês e o dia da data atual ainda não tiverem passado no ano corrente, ajustando a idade corretamente.
df.loc[df['data_ajustada'] > 100, 'data_ajustada'] = np.nan # Define valores maiores que 100 na coluna 'data_ajustada' como NaN, tratando casos de idades excessivamente altas como inválidos.

# Corrigir campos com múltiplas informações 
df['endereco_curto'] = df['endereco'].apply(lambda x: x.split('\n')[0].strip())
df['bairro'] = df['endereco'].apply(lambda x: x.split('\n')[1].strip() if len(x.split('\n')) > 1 else 'Desconhecido')
df['estado_sigla'] = df['endereco'].apply(lambda x: x.split(' / ')[1].strip() if len(x.split(' / ')) > 1 else 'Desconhecido')

# Verificando a formatação do endereço 
df['endereco_curto'] = df['endereco_curto'].apply(lambda x: 'Endereço inválido' if len(x) > 50 or len(x) < 5 else x)

# Corrigir dados de cpf possivelmente invalidos 
df['cpf'] = df['cpf'].apply(lambda x: x if len(x) == 14 else 'CPF inválido') 

estados_br = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
df['estado_sigla'] = df['estado_sigla'].apply(lambda x: x if x in estados_br else 'Desconhecido')

# Printando os dados tratados 
print('Dados tratados: \n', df.head())

# Salvando em arquivo CSV todo tratamento feito
df['cpf'] = df['cpf_mascara']
df['data'] = df['data_ajustada']
df['endereco'] = df['endereco_curto']
df['estado'] = df['estado_sigla']
df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'bairro', 'estado']]
df_salvar.to_csv('clientes_tratados.csv', index=False)
