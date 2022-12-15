import pandas as pd

notas = pd.read_csv("ratings.csv")
print(notas.head())
notas.columns = ["usuarioId", "filmeId", "nota", "momento"]
notas.nota.unique()
notas.nota.value_counts()
print(notas.nota.mean())
print(notas.nota.median())