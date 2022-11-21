import datetime

import pandas as pd

date = "Dt Negociação"
preco = "Preço"
compra = "Financeiro Compra"
venda = "Financeiro Venda"


with open('test.csv', 'r') as file:
    text = file.read()
    text = text.replace('"', '');
    text = text.replace('.', '');
    text = text.replace(',', '.');
    text = text.replace(';', ',');


with open('prepared.csv', 'w') as file:
    file.write(text)

dataFrame = pd.read_csv("./prepared.csv", encoding='latin-1')

# Unnecessary now that I'm creating a "prepared.csv" file
# print(dataFrame.info());
# dataFrame[compra] = dataFrame[compra].str.replace('.', '', regex=True);
# dataFrame[compra] = dataFrame[compra].str.replace(',', '.');
# dataFrame[compra] = pd.to_numeric(dataFrame[compra], errors='coerce')
#
# dataFrame[venda] = dataFrame[venda].str.replace('.', '', regex=True);
# dataFrame[venda] = dataFrame[venda].str.replace(',', '.');
# dataFrame[venda] = pd.to_numeric(dataFrame[venda], errors='coerce')
#
# dataFrame[preco] = dataFrame[preco].str.replace('.', '', regex=True);
# dataFrame[preco] = dataFrame[preco].str.replace(',', '.');
# dataFrame[preco] = pd.to_numeric(dataFrame[preco], errors='coerce')

print('Digite o mes para analisar (int)')
month = int(input())

test = pd.to_datetime(dataFrame[date], format='%d/%m/%Y')
dataFrame[date] = pd.to_datetime(dataFrame[date], format='%d/%m/%Y')

filteredDataFrame = dataFrame[dataFrame[date].dt.month == month]

#print(filteredDataFrame)

#print('Total Compra')
#print(filteredDataFrame[compra].sum().round(2))
#print('Total Venda')
#print(filteredDataFrame[venda].sum().round(2))

print(dataFrame.groupby(['Ativo'])[compra].sum()-dataFrame.groupby(['Ativo'])[venda].sum())

