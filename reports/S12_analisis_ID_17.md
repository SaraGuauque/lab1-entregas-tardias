# Interpretación de resultados | Semana 12 | ID 17

**Estudiante:** Sara Valentina Guauque Zarrate  
**Fuente:** ejecución real con Olist, semilla 1017, muestra de 35.000 pedidos.  
**Evaluación:** conjunto de validación de 5.250 pedidos, sin utilizar los 5.250 reservados para prueba.

## 6. Interpretación de negocio

**1. Compare la regresión logística con el modelo de referencia utilizando Accuracy, Recall y F1. Justifique su elección de `class_weight`.**

Cuando comparé los modelos, me di cuenta de que la Accuracy, por sí sola, puede dar una impresión equivocada. El modelo de referencia acertó el 93,24 % de los pedidos, pero tuvo un Recall de 0 % y un F1 de 0 %. Es decir, como casi todos los pedidos llegan a tiempo, podía acertar mucho sin detectar ni una sola entrega tardía. La regresión logística sin ponderación tuvo un comportamiento parecido: 93,22 % de Accuracy, pero también 0 % de Recall.

Por eso escogí `class_weight='balanced'`. Aunque la Accuracy bajó al 65,22 %, el modelo logró identificar 208 de los 355 pedidos que realmente llegaron tarde. Su Recall fue 58,59 % y su F1 fue 18,55 %, mejores para el objetivo de detectar retrasos. Eso sí, la Precision fue de apenas 11,02 %, así que todavía genera muchas alertas que no corresponden a retrasos reales. Para mí es un mejor punto de partida para este reto, pero no lo consideraría listo para usar en una empresa sin reducir esas falsas alarmas.

**2. Analice qué tipo de pedidos presenta mayor error según los segmentos estudiados. ¿Cómo se relaciona esto con el costo de falsos positivos y falsos negativos?**

Al revisar los errores por grupos, vi que agosto fue el mes con la mayor tasa: el modelo se equivocó en 279 de 584 pedidos, un 47,77 %. Entre los estados con al menos 100 pedidos de validación, Río de Janeiro (RJ) tuvo la tasa de error más alta, 69,13 %, sobre 635 pedidos. Esto no quiere decir que agosto o Río de Janeiro causen retrasos; únicamente muestra en qué grupos se equivocó más el modelo con los datos que analicé.

También revisé los dos tipos de error. Hubo 1.679 falsos positivos, que son pedidos que el modelo marcó como tardíos pero llegaron a tiempo, y 147 falsos negativos, que son retrasos reales que el modelo no detectó. Con los costos que propone el ejercicio, los falsos positivos suman R$ 13.432 (1.679 × 8) y los falsos negativos R$ 5.145 (147 × 35). En total son R$ 18.577, mientras que el modelo de referencia costaría R$ 12.425 según ese mismo supuesto.

Mi conclusión es que conseguimos detectar más entregas tardías, pero a cambio generamos demasiadas alertas innecesarias. Por eso no basta con mirar el Recall: también hay que revisar cuántos errores estamos cometiendo y cuánto costarían.

**3. Proponga una mejora concreta para la semana 13 y explique cómo la verificaría utilizando la misma validación.**

Para la semana 13 probaría mejorar la regresión logística que ya construí, en vez de cambiar todo el proyecto. Empezaría comparando varios valores de `C` (0,1; 1 y 10), porque ese parámetro controla la regularización del modelo. Además, revisaría si cambiar el umbral con el que se marca un pedido como tardío ayuda a disminuir las falsas alarmas, sin dejar de detectar tantos retrasos.

Lo comprobaría entrenando cada alternativa con los mismos 24.500 pedidos y comparándola en los mismos 5.250 de validación. Me fijaría especialmente en Recall, F1 y en el costo de los falsos positivos y negativos. Mi punto de partida es Recall de 58,59 %, F1 de 18,55 % y costo de R$ 18.577. No daría por hecho que el ajuste mejora el modelo: tendría que demostrarlo con esas métricas. Los 5.250 pedidos de prueba los dejaría sin tocar hasta la evaluación final de la semana 16.

## Limitaciones que debo explicar

El análisis solamente contiene pedidos que ya fueron entregados. Las tasas de error por mes y estado muestran asociaciones en la muestra, no causas demostradas. Los costos de R$ 8 y R$ 35 por error son valores hipotéticos del ejercicio, no cifras oficiales de Olist. Además, se utilizó una partición aleatoria para validar, por lo que todavía falta evaluar qué sucede al generalizar a otros periodos.

*Estas respuestas están redactadas a partir de las cifras reales del laboratorio. Antes de sustentar, debo leerlas y asegurarme de comprenderlas.*
