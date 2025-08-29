
# Primer contacto con Machine Learning 

Este proyecto es mi **primer acercamiento real a Machine Learning**.  
La idea es predecir el **precio de una casa en función de su tamaño (m²)** usando **Regresión Lineal**.

---

##  Tecnologías utilizadas
- Python 3.13  
- [NumPy](https://numpy.org/) → operaciones matemáticas  
- [Pandas](https://pandas.pydata.org/) → manejo de datos  
- [scikit-learn](https://scikit-learn.org/) → modelo de regresión lineal  
- [Matplotlib](https://matplotlib.org/) → visualización de resultados  

---

##  Estructura del proyecto
```
Primer proyecto/
│── Entrenamiento.py   # Script principal del modelo
│── README.md          # Documentación
```

---

## ⚙️ Instalación
Clona este repositorio y entra a la carpeta:

```bash
git clone <url-del-repo>
cd "Primer proyecto"
```

Instala las dependencias:

```bash
pip install numpy pandas scikit-learn matplotlib
```

---

## ▶ Ejecución
Corre el script en consola:

```bash
python Entrenamiento.py
```

---

##  Resultados esperados
1. En consola verás:
   - El **coeficiente (pendiente)** de la recta.  
   - El **intercepto**.  
   - El **error cuadrático medio (MSE)**.  
   - El **R²** (qué tan bien explica el modelo los datos).  

2. Se mostrará una gráfica:  
   - Puntos azules = datos reales.  
   - Línea roja = predicciones del modelo.  

Ejemplo:

![Gráfico regresión](https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Linear_regression.svg/512px-Linear_regression.svg.png)

---

##  Qué aprendí
- Cómo estructurar un dataset con **Pandas**.  
- Cómo entrenar un modelo de **Regresión Lineal** en `scikit-learn`.  
- Cómo dividir datos en **entrenamiento** y **prueba**.  
- Cómo evaluar un modelo con métricas básicas.  
- Cómo visualizar resultados con **Matplotlib**.  

---

##  Próximos pasos
- Usar más variables (habitaciones, antigüedad, ubicación).  
- Probar datasets reales de `scikit-learn` como **Boston Housing** o **Iris**.  
- Implementar otros algoritmos (árboles de decisión, regresión logística).  

---
