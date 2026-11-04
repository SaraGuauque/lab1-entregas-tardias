# Interpretacion de resultados | S12 | ID 17

**Borrador automatizado basado en la ejecucion:** revisar, reformular y sustentar personalmente antes de entregar.

## Pregunta 1

En los 5,250 pedidos de validacion, el clasificador de referencia obtuvo Accuracy=0.932, Recall=0.000 y F1=0.000. La regresion logistica seleccionada obtuvo Accuracy=0.652, Recall=0.586 y F1=0.186; AP=0.131 y ROC-AUC=0.684. Utilice `class_weight='balanced'` porque fue la configuracion con mejor F1 en la comparacion de validacion (con Recall como desempate). Una Accuracy mayor, por si sola, no significa que se detecten retrasos: el enfoque es identificar la clase minoritaria sin usar los datos de prueba.

## Pregunta 2

El mes con mayor porcentaje de errores fue 8 con 47.77% (279 errores de 584 pedidos). Entre los estados con al menos 100 pedidos (o todos, si no hay ninguno), el de mayor tasa de error fue RJ: 69.13% con 635 pedidos. La matriz de confusion arrojo 1679 falsos positivos y 147 falsos negativos; sus costos ilustrativos fueron R$ 13,432 y R$ 5,145, para un total de R$ 18,577 frente a R$ 12,425 del modelo mayoritario. Un falso negativo cuesta 35 reales y un falso positivo 8, pero deben considerarse tanto su cantidad como la tasa de error de cada segmento. Las diferencias observadas son descriptivas, no causales.

## Pregunta 3

Para la semana 13 comparare regularizacion de la regresion logistica (C = 0.1, 1, 10) y un tratamiento de categorias poco frecuentes. Mantendre los mismos 35.000 pedidos, la semilla, los predictores y los 24.500/5.250/5.250 registros de entrenamiento/validacion/prueba. La linea base a superar es F1=0.186, Recall=0.586, AP=0.131 y costo ilustrativo de R$ 18,577. Solo entrenare con train y evaluare alternativas sobre valid; no usaremos el test antes del cierre de la semana 16.

## Limitaciones

La muestra solo incluye pedidos entregados; los costos de R$ 8 y R$ 35 son supuestos didacticos, no cifras oficiales de Olist. La validacion aleatoria no demuestra desempeño prospectivo. Las 28 variables excluyen informacion futura de despacho y entrega.
