# Semana 14 - Laboratorio 2: instrucciones de ejecución

**Estudiante:** Sara Valentina Guauque Zarrate  
**ID:** 17 · **Semilla:** 1017  
**Fuente académica:** Semana14_Olist.html; Lectura_Apoyo_S14.html (Elias Buitrago Bolivar).

## Objetivo

Comprobar si aplicar PCA con 90 % de varianza explicada y modificar la regularización de una regresión logística mejora la identificación de pedidos tardíos de Olist, y qué alternativa presenta el menor costo ilustrativo de errores.

## Reglas del experimento

- Mantener la muestra S12 (35.000, huella `55ced66ce4f4`), con 24.500 / 5.250 / 5.250 de entrenamiento / validación / prueba.
- Ajustar imputación, escala y PCA **solo** con entrenamiento, nunca con validación ni prueba.
- Conservar 24 predictores numéricos y 4 categóricos; PCA solo sobre los numéricos.
- Probar exactamente cuatro configuraciones: A (sin PCA, C=1), B (PCA, C=1), C (PCA, C=0,1), D (PCA, C=10). Todas usan `class_weight='balanced'` y umbral 0,50.
- Comparar Accuracy, Precision, Recall, F1, AP y el costo **8 × FP + 35 × FN**.
- Contrastar por KS `valor_flete` entre train y valid con alfa 0,05. Reportar D, p, la decisión y el límite de la prueba.
- Los costos son académicos, no reales de Olist; el test se reserva.

## Evidencia del repositorio

| Archivo | Función |
|---|---|
| `notebooks/S14_Lab2_PCA_Validacion_ID_17.ipynb` | Solución ejecutable con salidas |
| `reports/S14_resultados_ID_17.json` | Configuración y métricas verificables |
| `reports/S14_experimentos_ID_17.csv` | Tabla de los cuatro modelos |
| `reports/S14_analisis_ID_17.md` | Interpretación y decisión |
| `reports/figuras/S14_*.png` | Curvas PCA y KS, comparación de métricas/costos |
| `scripts/ejecutar_s14.py`, `scripts/verificar_s14.py` | Ejecución y pruebas |
| `.github/workflows/ejecutar_olist_s14_id17.yml` | Automatización reproducible |

## Cómo volver a ejecutar

Desde GitHub, abrir **Actions → S14 - PCA y validación - ID 17 → Run workflow**. El flujo descarga los CSV públicos de la revisión fijada, ejecuta todas las celdas, comprueba las evidencias, guarda un artefacto descargable y registra los resultados en la rama main.

También puede abrirse el notebook desde Google Colab y ejecutar «Entorno de ejecución → Ejecutar todas» con acceso a Internet. Evite compartir los CSV originales.

## Interpretación de negocio

La decisión final debe justificar la elección de modelo sobre la comparación A–D con la misma validación y el mismo umbral, especialmente cuando F1 y costo no recomiendan la misma configuración. Una mejora de PCA no se presupone: se mide. KS indica diferencias en la distribución del flete, no que un modelo supere estadísticamente a otro.

**Entrega:** enlace al commit que contiene notebook y reportes, según las instrucciones del profesor en Teams. La guía de clase propone el domingo 15 de noviembre de 2026; debe confirmarse el plazo final en Teams.
