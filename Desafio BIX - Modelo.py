#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import requests
from io import StringIO
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.impute import SimpleImputer
import joblib
import numpy as np


# In[2]:


# Link raw do arquivo CSV no GitHub
url = 'https://raw.githubusercontent.com/Rothier/DesafioBIX/main/air_system_present_year.csv'
token = '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'

# Fazer o download da planilha
headers = {'Authorization': f'token {token}'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = pd.read_csv(StringIO(response.text))
else:
    print(f"Erro ao carregar o arquivo CSV: {response.status_code} - {response.reason}")
    exit()


# In[3]:


# Função para verificar se um valor é numérico
def is_numeric(val):
    try:
        float(val)
        return True
    except (ValueError, TypeError):
        return False

# Função para limpar os dados
def clean_data(df):
    for column in df.columns:
        if column != 'class':
            # Identificar e substituir valores não numéricos e longos por NaN
            df[column] = df[column].apply(lambda x: x if is_numeric(x) and len(str(x)) < 100 else np.nan)
    return df


# In[4]:


# Substituir 'na' por NaN e limpar dados malformados
data.replace('na', np.nan, inplace=True)
data = clean_data(data)

# Verificar e imprimir colunas com valores ausentes
print("Colunas com valores ausentes:")
missing_data_columns = data.columns[data.isna().any()].tolist()
for column in missing_data_columns:
    missing_count = data[column].isna().sum()
    print(f"{column}: {missing_count} valores ausentes")


# In[5]:


# Dividir os dados em features e target
X = data.drop('class', axis=1)
y = data['class']

# Imputar valores ausentes com a média das colunas numéricas
imputer = SimpleImputer(strategy='mean')
X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

# Converter a coluna 'class' para valores binários: 'pos' = 1, 'neg' = 0
y = y.apply(lambda x: 1 if x == 'pos' else 0)


# In[6]:


# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)


# In[7]:


# Avaliar o modelo
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Salvar o modelo treinado
joblib.dump(model, 'modelo_random_forest.pkl')


# In[ ]:




