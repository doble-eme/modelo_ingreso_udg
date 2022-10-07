# Modelo Ingreso UDG

Este repositorio contiene los datos, análisis y aplicación de modelos de aprendizaje automático utilizados para elaborar un sistema que determine las posibilidades de ingreso a la Universidad de Guadalajara para distintas carreras de nivel licenciatura.

## Obtención de los Datos

Los datos para alimentar al algoritmo de árbol de decisión fueron tomados de la página de [estadísticas de la Universidad de Guadalajara](http://www.escolar.udg.mx/estadisticas). Se utilizaron datos de un periodo de 10 años para entrenar el algoritmo y los datos del útlimo calendario disponible para hacer pruebas.

## Análisis Inicial de los Datos

Para determinar las variables de interés se realizó un análisis de estadística descriptiva y posteriormente se procedió a limpiar los datos y procesarlos usando la librería Pandas en Jupyter Notebooks.

## Entrenamiento del modelo de árbol de decisión

Para realizar el entrenamiento del modelo se utilizó la función `DecisionTreeClassifier()` de la librería Scikit Learn.

## Interfaz gráfica

Una vez entrenado el modelo se guardó en un archivo utilizando el módulo de Python Pickle y para generar la interfaz gráfica que interactúa con el modelo se utilizó el framework Flask.
