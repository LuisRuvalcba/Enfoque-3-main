from sklearn.ensemble import AdaBoostClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generar datos de ejemplo para clasificación
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)

# Dividir datos en conjunto de entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializar modelo AdaBoost para clasificación
modelo = AdaBoostClassifier(n_estimators=50, random_state=42)

# Entrenar el modelo
modelo.fit(X_entrenamiento, y_entrenamiento)

# Predecir clases en el conjunto de prueba
predicciones = modelo.predict(X_prueba)

# Calcular precisión del modelo
precision = accuracy_score(y_prueba, predicciones)
print("Precision del modelo:", precision)
