# SISTEMA DE VENTAS DE SUSTANCIAS QUÍMICAS

## Integrantes
- Emiliano Rojas

## Escenario elegido
Escenario B – Análisis de Ventas de una Pequeña Empresa.

## Descripción del proyecto
El proyecto analiza un conjunto de datos simulados de ventas de sustancias químicas.  
El objetivo es calcular indicadores básicos para interpretar el desempeño comercial.

## Dataset utilizado
El archivo de datos se encuentra en:

datos/dataset.csv

Contiene información de:
- mes
- producto
- unidad
- cantidad vendida
- precio

## Indicadores calculados
El script calcula:
- ventas totales
- producto más vendido
- ventas por mes

## Estructura del repositorio

datos/
dataset.csv

scripts/
analisis_datos.py

resultados/
grafico_resultados.png

## Instrucciones de ejecución
Desde Google Colab, ubicarse en la carpeta del repositorio y ejecutar:

python scripts/analisis_datos.py

El script lee el dataset, calcula los indicadores y genera el gráfico en la carpeta resultados.
