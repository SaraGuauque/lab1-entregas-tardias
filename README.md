# Data Analytics ML Challenge | Olist

### Laboratorio individual 1 - Semana 12, 2026-2

**Estudiante:** Sara Valentina Guauque Zarrate  
**Programa:** Ingeniería de Sistemas y Computación  
**Universidad:** Universidad Central  
**Profesor:** Elias Buitrago Bolivar

## Sobre el proyecto

Construyo modelos supervisados para anticipar si un pedido de comercio electrónico se entregará después de la fecha prometida. Utilizo el conjunto de datos real y anonimizado **Brazilian E-Commerce Public Dataset by Olist**. Cada fila del análisis equivale a un pedido; los artículos y pagos se agregan por pedido para prevenir duplicados.

La variable objetivo es `is_late` (1 = entrega después de la fecha estimada, 0 = a tiempo). El modelo usa **28 predictores** (24 numéricos y 4 categóricos) conocidos al confirmar el pago. Se excluyen variables posteriores a la compra para evitar fuga de información.

> **Identificador individual:** `17` (confirmado por la estudiante). **Semilla:** `1017`. La muestra de 35.000 pedidos se genera al ejecutar el notebook con los CSV reales fijados en la revisión de Olist usada por el docente. No se utilizan los reportes ni resultados de otros estudiantes.

> **Estado del cálculo:** el código está completo y probado con datos sintéticos de control, pero las métricas individuales reales se generan al ejecutar con Olist. Los datos originales no se incluyen en este repositorio.

## Estructura

```text
Sara_Valentina_Guauque_Zarrate_ML_Challenge/
|-- .github/workflows/tests.yml
|-- .github/workflows/ejecutar_olist_id17.yml
|-- .gitignore
|-- data/
|   |-- raw/.gitkeep                 # CSV originales locales: no se publican
|   `-- processed/.gitkeep           # Archivos regenerables: no se publican
|-- docs/
|   |-- Guia_Olist_S12.html          # Guion y diccionario entregados en clase
|   |-- PASOS_ENTREGA.md             # Guía paso a paso en Windows/Colab/GitHub
|   `-- RESULTADOS_Y_SUSTENTACION.md  # Guía de interpretación
|-- notebooks/
|   `-- S12_ML_Challenge.ipynb       # Notebook oficial, actividades 1-4 completas
|-- src/
|   |-- __init__.py
|   `-- evaluacion.py                 # Utilidades reutilizables
|-- tests/
|   |-- test_evaluacion.py           # Pruebas de consistencia sin datos externos
|   `-- test_configuracion_id17.py   # Control de ID 17
|-- scripts/
|   |-- ejecutar_lab.py              # Ejecutar el notebook con ID 17
|   `-- verificar_entrega.py         # Verificar resultados individuales
|-- reports/
|   `-- .gitkeep                     # Se genera JSON + análisis + tablas + figuras
|-- requirements.txt
`-- README.md
```

## Metodología de S12

1. **Carga:** lectura de las siete tablas oficiales desde la revisión fija de GitHub.
2. **Preparación:** agregación por `order_id`, control de duplicados, cálculo de objetivos y 28 variables.
3. **Muestra individual:** 35.000 pedidos estratificados; semilla `1000 + ID_ESTUDIANTE`.
4. **Separación:** 24.500 entrenamiento, 5.250 validación y 5.250 prueba (reservada hasta S16).
5. **Modelado:** referencia `DummyClassifier`; regresión logística con y sin `class_weight='balanced'`; selección por mayor F1 de validación, con Recall como desempate.
6. **Evaluación:** Accuracy, Precision, Recall, F1, ROC-AUC, AP y matriz de confusión. Regresión `Ridge` y MAE en días.
7. **Negocio:** errores por mes y estado, totales, FP, FN, costos hipotéticos de R$ 8 por FP y R$ 35 por FN.
8. **Evidencia:** autoverificaciones `assert` originales, JSON individual y borrador de interpretación con cifras reales.

La selección de la ponderación se hace solo con **validación**, no con prueba. El conjunto `test` queda reservado para la semana 16.

## Ejecución en Google Colab

Abra `notebooks/S12_ML_Challenge.ipynb` en Colab. La celda de **Muestra individual** ya contiene `ID_ESTUDIANTE = 17`. Ejecute **Entorno de ejecución > Ejecutar todas**. El notebook descarga automáticamente los CSV (requiere internet), entrena los modelos, genera las tablas y verifica todas las aserciones. Guarde el notebook ejecutado en GitHub y suba el reporte JSON desde `reports/`.

Se generan adicionalmente dos archivos CSV de segmentación, imágenes y un borrador de respuestas con datos individuales; el borrador debe revisarse y personalizarse antes de la entrega.

## Ejecutar con datos reales directamente en GitHub (sin instalar Python)

El repositorio incluye `.github/workflows/ejecutar_olist_id17.yml`. Cuando haya subido la carpeta a GitHub, abra **Actions > Generar resultados reales - ID 17 > Run workflow**. La acción descarga los siete CSV originales en el equipo temporal de GitHub, ejecuta todas las celdas del notebook con la semilla 1017, comprueba el JSON y agrega el notebook ejecutado y los reportes al mismo repositorio mediante un commit automático. No se publican los CSV grandes.

Esta opción necesita que GitHub Actions tenga permiso de escritura en el repositorio. Si los permisos de tu cuenta no lo permiten, usa Colab o ejecuta localmente y sube los resultados manualmente.

## Ejecución local (Windows / PowerShell)

```powershell
python -m pip install -r requirements.txt
python -m pytest -q
python scripts/ejecutar_lab.py --id 17
```

Se utiliza el ID **17**, confirmado por la estudiante. El script ejecuta todo el notebook, conserva las salidas en el `.ipynb`, anota cifras verificadas en las tres respuestas Markdown (como borrador editable) y guarda resultados en `reports/`. Requiere conexión a los datos de Olist, salvo que use `OLIST_DATA_DIR` apuntando a los CSV originales locales.

**La entrega ejecutada requiere** `reports/S12_resultados_ID_17.json`, generado con los CSV reales de Olist (no con datos de ejemplo).

## Entregables finales

- [ ] Notebook final `.ipynb` ejecutado de principio a fin sin errores.
- [x] ID 17 confirmado; semilla 1017 configurada. Huella pendiente de la ejecución real.
- [ ] Cuatro actividades completadas, `assert` superadas.
- [ ] Tres respuestas interpretativas revisadas con cifras propias.
- [ ] `reports/S12_resultados_ID_17.json` y evidencias registradas en GitHub.
- [ ] Al menos dos commits descriptivos de trabajo: modelo y evaluación.

## Continuidad S13-S16

S12 establece la línea base; S13 ensayará mejoras/regularización; S14 validación e incertidumbre; S15 redes neuronales; S16 integrará resultados y evaluará sobre prueba, conservando la semilla, las variables y las particiones de S12.

## Datos y créditos

**Fuente:** Olist (2018), *Brazilian E-Commerce Public Dataset by Olist*, Kaggle (CC BY-NC-SA 4.0). Los siete CSV de trabajo se descargan de `spdrio/Brazilian-E-Commerce-Public-Dataset-by-Olist`, revisión fija `fa0cc6d1aff713d3c8b9a1e633b56889881848bf`, tal como exige la guía docente.

**Documento docente:** Elias Buitrago Bolivar, guía de Olist S12 y *ML Challenge DatAn 3C 2026-2*, Universidad Central. Se preservó la estructura metodológica y la autoverificación oficial.