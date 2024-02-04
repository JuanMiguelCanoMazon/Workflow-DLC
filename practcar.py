import pandas as pd
import matplotlib.pyplot as plt

file_path = 'carsales.csv'
data = pd.read_csv(file_path)

# Número de automóviles vendidos por marca
# agrupando para ello los datos por 'Company'
ventas_por_marca = data.groupby('Company').size()

plt.figure(figsize=(10, 6))
ventas_por_marca.plot(kind='bar')
plt.title('Ventas de coches por marca')
plt.xlabel('Marca')
plt.ylabel('Número de coches vendidos')
plt.xticks(rotation=45)
plt.show()