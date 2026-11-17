# Laboratorio 2 · Semana 14 · Olist · ID 17

**Estudiante:** Sara Valentina Guauque Zarrate
**Datos:** 35.000 pedidos reales; 24.500 train, 5.250 valid y 5.250 test reservado.
**Semilla:** 1017 · **Huella:** 55ced66ce4f4

## PCA
Partí de 24 variables numéricas y PCA conservó 15 componentes, con 90.93% de varianza explicada.
Al comparar B (PCA) con A (sin PCA), el cambio fue de -0.70 puntos porcentuales en F1 y -1.41 puntos en Recall. Conservar varianza no garantiza mejorar la detección de entregas tardías.

## Cuatro modelos y decisión
Todos los modelos usaron la misma validación, class_weight=balanced y umbral 0,50.

| Modelo | Accuracy | Precision | Recall | F1 | AP | FP | FN | Costo R$ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A_sin_PCA_C1 | 0.653 | 0.111 | 0.589 | 0.186 | 0.131 | 1678 | 146 | 18,534 |
| B_PCA90_C1 | 0.645 | 0.106 | 0.575 | 0.179 | 0.118 | 1715 | 151 | 19,005 |
| C_PCA90_C0_1 | 0.645 | 0.107 | 0.577 | 0.180 | 0.117 | 1716 | 150 | 18,978 |
| D_PCA90_C10 | 0.645 | 0.107 | 0.575 | 0.180 | 0.117 | 1711 | 151 | 18,973 |

Entre A–D, la alternativa con menor costo fue **A_sin_PCA_C1**, con R$ 18,534 calculados a partir de 1678 falsos positivos y 146 falsos negativos. La de mayor F1 fue A_sin_PCA_C1. La elección responde al criterio de costo de esta actividad, no a una superioridad estadística demostrada.

## Prueba KS: flete entre entrenamiento y validación
**H0:** ambas distribuciones poblacionales son iguales. **H1:** son diferentes. **α:** 0.05.
El estadístico fue D=0.009333 y el valor p=0.842071. Al 5 % no encontramos evidencia suficiente para rechazar la hipótesis de una distribución común de fletes. Esto no demuestra igualdad.
KS compara distribuciones de una variable, no desempeño de clasificadores. Los importes repetidos pueden afectar el valor p de la prueba clásica.

## Alcance y limitaciones
No se utilizó el conjunto de prueba para ajustar, escoger ni evaluar los modelos. El análisis incluye pedidos efectivamente entregados; los costos R$ 8 y R$ 35 son supuestos didácticos, no cifras contables de Olist. 
