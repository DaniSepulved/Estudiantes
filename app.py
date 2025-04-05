import streamlit as st
import pandas as pd
from io import StringIO

datos = """
id,nombre,edad,ciudad,promedio,asistencia
1,Juan Pérez,17,Bogotá,4.5,0.95
2,María Gómez,16,Medellín,3.8,0.88
3,Carlos López,18,Cali,4.2,0.92
4,Ana Martínez,15,Barranquilla,3.5,0.85
5,Pedro Sánchez,19,Cartagena,4.8,0.97
6,Laura Rodríguez,17,Bogotá,4.0,0.90
7,Diego Torres,16,Medellín,3.9,0.87
8,Sofía Díaz,18,Cali,4.3,0.93
9,Andrés Herrera,15,Barranquilla,3.7,0.86
10,Valentina Ruiz,19,Cartagena,4.6,0.96
11,Jorge Ramírez,17,Bogotá,4.1,0.91
12,Camila Vargas,16,Medellín,3.6,0.89
13,Mateo Castro,18,Cali,4.4,0.94
14,Lucía Morales,15,Barranquilla,3.4,0.84
15,Santiago Ortiz,19,Cartagena,4.7,0.98
16,Isabella Peña,17,Bogotá,4.2,0.92
17,Sebastián Gil,16,Medellín,3.8,0.88
18,Paula Rincón,18,Cali,4.5,0.95
19,Felipe Arias,15,Barranquilla,3.9,0.87
20,Daniela Muñoz,19,Cartagena,4.9,0.99
21,Julián Vega,17,Bogotá,4.0,0.90
22,Natalia Cordero,16,Medellín,3.7,0.86
23,Miguel Salazar,18,Cali,4.3,0.93
24,Carolina Pineda,15,Barranquilla,3.5,0.85
25,Tomás Mendoza,19,Cartagena,4.6,0.96
26,Clara Ospina,17,Bogotá,4.1,0.91
27,Luis Escobar,16,Medellín,3.8,0.88
28,Emma Rojas,18,Cali,4.4,0.94
29,Gabriel Duarte,15,Barranquilla,3.6,0.87
30,Valeria Sierra,19,Cartagena,4.8,0.97
31,David Meza,17,Bogotá,4.2,0.92
32,Renata Londoño,16,Medellín,3.9,0.89
33,Nicolás Bravo,18,Cali,4.5,0.95
34,Mariana Tovar,15,Barranquilla,3.7,0.86
35,Juan Camilo Zuluaga,19,Cartagena,4.7,0.98
36,Sara Bermúdez,17,Bogotá,4.0,0.90
37,Héctor Parra,16,Medellín,3.8,0.88
38,Lina Agudelo,18,Cali,4.3,0.93
39,Simón Restrepo,15,Barranquilla,3.5,0.85
40,Andrea Hoyos,19,Cartagena,4.9,0.99
41,Esteban Quintero,17,Bogotá,4.1,0.91
42,Mónica Cano,16,Medellín,3.6,0.89
43,Javier Paredes,18,Cali,4.4,0.94
44,Patricia León,15,Barranquilla,3.9,0.87
45,Leonardo Giraldo,19,Cartagena,4.6,0.96
46,Beatriz Uribe,17,Bogotá,4.2,0.92
47,Rafael Núñez,16,Medellín,3.7,0.86
48,Claudia Zapata,18,Cali,4.5,0.95
49,Iván Córdoba,15,Barranquilla,3.8,0.88
50,Angela Florez,19,Cartagena,4.8,0.97
"""

# Convertir el texto a un DataFrame
df = pd.read_csv(StringIO(datos.strip()))

# # Guardar como CSV
df.to_csv("estudiantes.csv", index=False)

lee = pd.read_csv("estudiantes.csv")

st.subheader("Primeras 5 filas del dataset")
st.write(lee.head())

st.subheader("Últimas 5 filas del dataset")
st.write(lee.tail(5))


# Informacion del dataset
st.subheader("Información del dataset")
st.text(df.info())

st.subheader("Información del dataset")
st.text(df.describe())


# Selección de columnas

st.subheader("Selección de columnas: Especie y Edad")
st.write(df[['nombre', 'edad', 'promedio']])


# Promedio

min_promedio = st.slider(
    "Selecciona el promedio mínimo:",
    min_value=float(df["promedio"].min()),
    max_value=float(df["promedio"].max()),
    value=4.0,
    step=0.1
)

estudiantes_filtrados = df[df["promedio"] >= min_promedio]
st.subheader(f"Estudiantes con promedio mayor o igual a {min_promedio}:")
st.write(estudiantes_filtrados)