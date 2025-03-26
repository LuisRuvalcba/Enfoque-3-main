# Importar librerías necesarias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Cargar conjunto de datos de precios de casas
datos = pd.read_csv('precios_casas.csv')

# Visualizar los primeros registros del conjunto de datos
print(datos.head())

# Separar características (X) y variable objetivo (y)
X = datos[['tamaño', 'num_habitaciones']]
y = datos['precio']

# Dividir datos en conjunto de entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar y entrenar modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X_entrenamiento, y_entrenamiento)

# Predecir precios de casas en el conjunto de prueba
predicciones = modelo.predict(X_prueba)

# Evaluar rendimiento del modelo
rendimiento = modelo.score(X_prueba, y_prueba)
print("Rendimiento del modelo:", rendimiento)
