import pandas as pd 

# Função para calcular o o cubo de um número
def eleva_cubo(x):
    return x ** 3

# Expressão de lambda para calcular o cubo de um número
eleva_cubo_lambda = lambda x: x ** 3

print(eleva_cubo(2))
print(eleva_cubo_lambda(2))

df = {'numeros': [1,2,3,4,5,10]}

df['cubo_funcao'] = df['numeros'].apply(eleva_cubo)
df['cubo_lambda'] = df['numeros'].apply(eleva_cubo_lambda)
print(df)

