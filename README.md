# Modelo de predicción UDG

Este repositorio contiene un modelo de predicción de regresión lineal para analizar las estadísticas de ingreso a las carreras de Licenciatura en Informática y Licenciatura en Ingeniería en Computación de la Universidad de Guadalajara (UdeG), en específico las que se ofertan en el Centro Universitario de Ciencias Exactas e Ingeniería (CUCEI). Los datos para alimentar el algoritmo fueron obtenidos del sitio de Estadísticas de la UdeG (http://www.escolar.udg.mx/estadisticas), y corresponden a los últimos 10 años (2010-2020).

El modelo utilizado es un modelo de aprendizaje supervisado, conocido como Regresión Lineal Simple. Las tecnologías y librerías utilizadas para este análisis son las siguientes:

- [Python 3](https://www.python.org)
- [Jupyter Notebooks](https://jupyter.org)
- [Pandas](https://pandas.pydata.org)
- [Numpy](https://numpy.org)
- [Matplotlib](https://matplotlib.org)
- [Sklearn](https://scikit-learn.org)

Este repositorio contiene los archivos Excel (`.xlsx`) con los datos primarios y los Jupyter Notebooks con el código utilizado para realizar el análisis.

## Obtención de los Datos

Como se mencionó antes, la información está disponible en la página de Estadísticas de la UdeG: http://escolar.udg.mx/estadisticas.

Los datos disponibles en esta fuente contienen información acerca de los estudiantes admitidos en los últimos 10 años: promedios mínimos por carrera y por centro universitario, número total de admitidos (hombres y mujeres) y número de admitidos por escuela de procedencia (públicas y privadas).

Esta información se encuentra en archivos Excel (`.xlsx`). El proceso de descarga consistió en descargar cada archivo de Excel individualmente, con lo que se obtuvo un total de 40 archivos `.xlsx`.

Estos 40 archivos de Excel pertenecen a dos categorías según el tipo de información que contienen:

-	Admitidos_por_procedencia_escolar_{año}.xlsx
-	Puntajes_minimos_CUs_{año}.xlsx

En los archivos de Admitidos por procedencia escolar se encuentra la información del total admitidos por cada centro universitario y por cada carrera, divididos en el número de mujeres y hombres que provienen de escuelas públicas o privadas, pertenecientes a la UDG o incorporadas, etcétera. 

Con estos datos obtendremos el número total de hombres y mujeres admitidos en los últimos diez años, así como el número de admitidos según su procedencia escolar y se procederá a alimentar el algoritmo para su procesamiento y análisis.

En los archivos de Puntajes mínimos por Centros Universitarios se encuentra la información relativa al puntaje mínimo requerido en cada periodo para ingresar a cada carrera de cada centro universitario. Contiene otros datos tales como el porcentaje de admisión o el cupo disponible en cada periodo.

El total de archivos recolectados contiene suficiente información para comenzar a procesar, organizar y posteriormente analizar para obtener resultados relevantes para el objetivo del proyecto. La información se encuentra dispersa en numerosos archivos, se hizo una limpieza de los datos para hacerlos consistentes ya que en su forma original no respetan una misma nomenclatura de los parámetros (en ocasiones el nombre de las carreras aparece completo, pero en otras aparece con abreviaciones; en otros casos las palabras que nombran a cada columna aparecen en mayúsculas y sin acentos, mientras que en otras aparecen en formato título y con acentos). Se uniformaron la nomenclatura de columnas, centros universitarios y nombres de carreras para facilitar la importación masiva de los datos.