# Laboratorio 2 · Semana 14 | Análisis de resultados

**Estudiante:** Sara Valentina Guauque Zarrate  
**ID:** 17 · **Semilla:** 1017  
**Fuente:** Olist, siete archivos CSV reales en revisión fija `fa0cc6d1…`  
**Muestra:** 35.000 pedidos · 24.500 entrenamiento · 5.250 validación · 5.250 prueba reservada  
**Huella reproducible:** `55ced66ce4f4`

## Interpretación personal de los resultados

### 1. PCA: ¿sirvió reducir las variables?

Al empezar, tenía 24 variables numéricas sobre el pedido, como el valor de los productos, el flete, el peso y el plazo prometido. Con PCA logré resumir esa información en **15 componentes**, conservando **el 90,93 % de la varianza**. Esto me mostró que algunas variables están relacionadas y que es posible trabajar con una representación más pequeña.

Sin embargo, cuando comparé el modelo sin PCA (A) con el que sí utiliza PCA (B), el F1 pasó de **18,64 % a 17,94 %** y el Recall bajó de **58,87 % a 57,46 %**. Además, el costo estimado aumentó de **R$ 18.534 a R$ 19.005**. Por eso, en mi caso, reducir dimensiones no significó mejorar las predicciones. Conservar mucha varianza no garantiza conservar precisamente la información que ayuda a reconocer una entrega tardía.

### 2. Cuatro modelos y decisión: ¿cuál escogería?

Probé las cuatro configuraciones que pidió el profesor. Todas usaron los mismos pedidos, `class_weight='balanced'` y el umbral 0,50; cambié únicamente PCA y el valor de regularización `C`.

| Modelo | Accuracy | Precision | Recall | F1 | AP | FP | FN | Costo |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **A · sin PCA, C=1** | **65,26 %** | **11,08 %** | **58,87 %** | **18,64 %** | **13,09 %** | **1.678** | **146** | **R$ 18.534** |
| B · PCA, C=1 | 64,46 % | 10,63 % | 57,46 % | 17,94 % | 11,78 % | 1.715 | 151 | R$ 19.005 |
| C · PCA, C=0,1 | 64,46 % | 10,67 % | 57,75 % | 18,01 % | 11,74 % | 1.716 | 150 | R$ 18.978 |
| D · PCA, C=10 | 64,53 % | 10,65 % | 57,46 % | 17,97 % | 11,74 % | 1.711 | 151 | R$ 18.973 |

Yo escogería **el modelo A** entre estos cuatro experimentos, porque obtuvo el **F1 más alto** y el **menor costo ilustrativo**. Detectó 209 de los 355 pedidos realmente tardíos, aunque también señaló equivocadamente 1.678 pedidos puntuales. Eso muestra que todavía necesitamos mejorar la precisión de las alertas.

Los cambios de `C` tampoco compensaron el efecto de PCA: C y D quedaron muy cerca de B, pero ninguno superó a A. No puedo decir que PCA sea malo en general; solamente que **no aportó una mejora en esta comparación concreta**.

### 3. Costos: ¿qué implica para una empresa?

El ejercicio asigna **R$ 8 por falso positivo** y **R$ 35 por falso negativo**. Para A, las falsas alarmas costarían R$ 13.424 y los retrasos no detectados R$ 5.110, sumando **R$ 18.534**. En B el costo total fue R$ 19.005, es decir, **R$ 471 más**.

Lo que más me llamó la atención es que, aunque A fue el mejor de los cuatro modelos, eso no significa que ya esté listo para una empresa. En la semana 12, la referencia que prácticamente no señalaba pedidos tardíos tenía un costo ilustrativo de **R$ 12.425** con estos mismos supuestos. Por eso mi recomendación sería mantener A como punto de partida, **reducir las falsas alarmas** y volver a comparar los costos antes de implementar una solución real. También habría que considerar beneficios y costos operativos que este ejercicio no incluye.

### 4. Prueba KS: ¿son distintas las distribuciones del flete?

Comparé `valor_flete` entre los 24.500 pedidos de entrenamiento y los 5.250 de validación usando Kolmogorov–Smirnov. Planteé como **H0** que ambos grupos tienen la misma distribución poblacional del flete y como **H1** que sus distribuciones son diferentes.

El resultado fue **D = 0,00933** y **p = 0,84207**. Como el valor p es mayor que 0,05, **no rechazo H0**: con esta prueba no encontré evidencia suficiente para afirmar que las distribuciones sean diferentes. Eso **no quiere decir que sean idénticas** ni que los modelos ya estén validados. KS compara la distribución de una variable, no demuestra que una regresión logística sea superior. Además, los valores monetarios repetidos y redondeados pueden afectar la interpretación de la prueba clásica.

### 5. Mi conclusión general

Este laboratorio me ayudó a comprobar algo importante: una técnica más elaborada no necesariamente mejora el resultado. **PCA redujo las variables numéricas de 24 a 15**, pero el modelo sin PCA siguió funcionando mejor bajo las condiciones de la actividad. Elegiría **A** para continuar el trabajo porque ofrece el mejor balance observado entre F1 y costo dentro de las cuatro opciones, aunque todavía presenta demasiadas falsas alarmas. Para una siguiente mejora revisaría el umbral de decisión y evaluaría sus efectos con una validación adecuada, sin tocar el conjunto de prueba reservado.

## Limitaciones del trabajo

Las comparaciones se hicieron con **la misma validación**, no con los pedidos de prueba final. No puedo atribuir causalidad a las variables ni afirmar superioridad estadística entre modelos solo por pequeñas diferencias de métricas. PCA fue ajustado únicamente con datos de entrenamiento y aplicado solo a las 24 variables numéricas; las 4 categóricas siguieron con One-Hot Encoding. Los costos de R$ 8 y R$ 35 son **supuestos del ejercicio académico**, no cifras reales de Olist. La prueba KS debe interpretarse con cautela porque el valor del flete puede contener empates.
