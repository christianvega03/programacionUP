# prompt: generar un código didáctico que involucre el uso de los módulos math, datetime, numpy y pandas.  Todas las librerías deben ser requeridas para la consecución de un único objetivo no pueden ser problemas aislados

import math
import datetime
import numpy as np
import pandas as pd

# Objetivo: Calcular la edad promedio de un grupo de personas y determinar cuántas
# cumplen años en cada mes, considerando solo los mayores de edad.

# Datos de ejemplo (simulando una base de datos)
data = {
    'Nombre': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Jona'],
    'Fecha de nacimiento': ['1995-03-15', '1988-11-20', '2004-07-02', '1992-05-10', '2000-01-25', '1998-09-21'],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Málaga','Zaragoza']
}

# Crear un DataFrame con Pandas
df = pd.DataFrame(data)

# Convertir la columna 'Fecha de nacimiento' a objetos datetime
df['Fecha de nacimiento'] = pd.to_datetime(df['Fecha de nacimiento'])

# Calcular la edad de cada persona
today = datetime.date.today()
df['Edad'] = df['Fecha de nacimiento'].apply(lambda dob: today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day)))

# Filtrar para incluir solo a los mayores de edad
df_mayores = df[df['Edad'] >= 18]

# Calcular la edad promedio de los mayores de edad
edad_promedio = np.mean(df_mayores['Edad'])
print(f"La edad promedio de las personas mayores de edad es: {edad_promedio:.2f} años")

# Determinar cuántas personas cumplen años en cada mes
cumpleaños_por_mes = df_mayores['Fecha de nacimiento'].dt.month.value_counts().sort_index()

# Imprimir resultados
print("\nNúmero de cumpleaños por mes:")
print(cumpleaños_por_mes)


# Ejemplo adicional con math y numpy (para ilustrar que pueden combinarse)
# Calcular la desviación estándar de las edades usando Numpy
desviacion_estandar = np.std(df_mayores['Edad'])
print(f"\nLa desviación estándar de la edad es: {desviacion_estandar:.2f}")

# Usamos la libreria math para redondear a dos decimales
redondeado = math.ceil(desviacion_estandar * 100)/100
print(f"Redondeado: {redondeado}")