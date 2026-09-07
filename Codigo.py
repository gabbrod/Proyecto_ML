import pandas as pd
import numpy as np

# cargar el dataset
url = 'https://raw.githubusercontent.com/gabbrod/Proyecto_ML/refs/heads/main/data/predictive_maintenance.csv'
df = pd.read_csv(url)

print(df.head(10))
print(df.shape)
print("---------------------------------------------")
print(df.dtypes)
print("---------------------------------------------")

for columna in df.columns:
    nulos = np.sum(pd.isnull(df[columna]))
    print(columna, "valores nulos: ", nulos)

#Estadística del dataset

print(df.describe())
print("---------------------------------------------")
columnas_interes = ['Type', 'Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]', 'Target']
for value in columnas_interes:
    frecuencia = df[value].value_counts()
    print(frecuencia)
print("---------------------------------------------")
print(df.groupby('Target').mean(numeric_only=True))
print("---------------------------------------------")

outliers_ambiente = df[(df["Air temperature [K]"] < 296.0) | (df["Air temperature [K]"] > 303.0)]
print("temperatura del ambiente por fuera del rango ", outliers_ambiente["Air temperature [K]"])

outliers_fabricación = df[(df["Process temperature [K]"]< 306.0) | (df["Process temperature [K]"] > 312.5)]
print("temperatura de la maquina por fuera del rango ", outliers_fabricación["Process temperature [K]"])