import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# 1. Dataset sencillo: precios de casas (tamaño en m² y precio)
data = {
    "tamaño_m2": [50, 60, 70, 80, 90, 100, 120, 150, 200],
    "precio_millones": [100, 120, 140, 160, 180, 200, 240, 300, 400]
}

df = pd.DataFrame(data)

# 2. Variables independientes (X) y dependiente (y)
X = df[["tamaño_m2"]]  # características
y = df["precio_millones"]  # etiqueta a predecir

# 3. Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Crear y entrenar modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# 5. Hacer predicciones
y_pred = modelo.predict(X_test)

# 6. Evaluar modelo
print("Coeficiente (pendiente):", modelo.coef_[0])
print("Intercepto:", modelo.intercept_)
print("Error cuadrático medio:", mean_squared_error(y_test, y_pred))
print("R²:", r2_score(y_test, y_pred))

# 7. Visualización
plt.scatter(X, y, color="blue", label="Datos reales")
plt.plot(X, modelo.predict(X), color="red", label="Modelo")
plt.xlabel("Tamaño (m²)")
plt.ylabel("Precio (millones)")
plt.legend()
plt.show()
