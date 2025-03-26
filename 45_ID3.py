from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos de flores Iris
iris = load_iris()

# Separar características (X) y etiquetas (y)
X = iris.data
y = iris.target

# Dividir datos en conjunto de entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar y entrenar modelo de árbol de decisión ID3
modelo = DecisionTreeClassifier(criterion='entropy')
modelo.fit(X_entrenamiento, y_entrenamiento)

# Predecir clases en el conjunto de prueba
predicciones = modelo.predict(X_prueba)

# Calcular precisión del modelo
precision = accuracy_score(y_prueba, predicciones)
print("Precision del modelo:", precision)
