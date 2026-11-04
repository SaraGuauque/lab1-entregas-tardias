# Pasos para entregar el laboratorio S12 en GitHub

## Paso 1. Identificador individual confirmado

- Estudiante: Sara Valentina Guauque Zarrate.
- **ID: 17** (confirmado expresamente por la estudiante).
- **Semilla de muestreo: 1017**, porque el profesor establece `1000 + ID_ESTUDIANTE`.
- Muestra de 35.000 pedidos, particiones 24.500 / 5.250 / 5.250.
- El notebook ya contiene `ID_ESTUDIANTE = 17`; no se debe cambiar entre semanas.

## Paso 2. Ejecutar y revisar el notebook

**Google Colab (recomendado por el docente):**

1. En Google Colab, use **Archivo > Subir cuaderno** y seleccione `notebooks/S12_ML_Challenge.ipynb`, o abra el archivo desde el repositorio GitHub.
2. Confirme que la celda de ID diga `ID_ESTUDIANTE = 17`.
3. Seleccione **Entorno de ejecución > Reiniciar sesión y ejecutar todo**.
4. Revise la tabla de comparación, matriz de confusión, métricas y los grupos por mes/estado.
5. Confirme que aparezca **Autoverificación superada.**
6. Descargue `reports/S12_resultados_ID_17.json`. Conserve también los dos CSV, las figuras y el borrador Markdown desde el explorador de archivos de Colab si quiere publicarlos.
7. Revise personalmente los tres párrafos de interpretación y agregue sus cifras en las celdas Markdown del notebook antes de guardar.
8. Guarde el `.ipynb` completo en el repositorio: **Archivo > Guardar una copia en GitHub** (si la opción está habilitada) o descargue el notebook y súbalo manualmente.

**Alternativa local (si tiene Python instalado):**

```powershell
cd Sara_Valentina_Guauque_Zarrate_ML_Challenge
python -m pip install -r requirements.txt
python -m pytest -q
python scripts/ejecutar_lab.py --id 17
```

El ID 17 ya esta establecido en el notebook. El ejecutor guarda el notebook final, los reportes y textos Markdown con valores reales; necesita acceso a internet o a los siete CSV originales en una carpeta local.

## Alternativa sin ejecutar localmente: GitHub Actions

1. Suba primero la carpeta del proyecto a un repositorio GitHub.
2. Entre en la pestaña **Actions**.
3. Seleccione **Generar resultados reales - ID 17** en el menú izquierdo.
4. Presione **Run workflow** y siga el estado de la ejecución.
5. Al terminar, busque en GitHub `reports/S12_resultados_ID_17.json`, `reports/S12_analisis_ID_17.md`, las tablas de segmentación, las figuras y `notebooks/S12_ML_Challenge.ipynb` actualizado con salidas.
6. Compruebe que las respuestas de interpretación reflejen sus propios resultados y personalícelas para poder sustentarlas.

El flujo exige acceso de red a `raw.githubusercontent.com` y permisos GitHub Actions `contents: write`. Si falla por permisos o red, ejecute en Colab o en su equipo.

## Paso 3. Crear el repositorio en GitHub

1. Inicie sesión en https://github.com/ y cree un repositorio público o privado según lo que pida el docente. Nombre sugerido: `Data-Analytics-ML-Challenge-Sara-Guauque`.
2. Para no perder subcarpetas ni archivos ocultos, use GitHub Desktop: **File > Clone repository** o clone por HTTPS.
3. Copie **el contenido** de esta carpeta dentro del repositorio clonado (no copie solamente el ZIP).
4. Realice un primer commit: `S12: modelo base y preparación de datos`.
5. Tras ejecutar y validar, haga otro commit: `S12: métricas, segmentos y reporte individual`.
6. Publique con **Push origin**. Compruebe desde el navegador que existen `notebooks/S12_ML_Challenge.ipynb` y `reports/S12_resultados_ID_17.json`.

**Alternativa con Git en PowerShell:**

```powershell
git init
git add .
git commit -m "S12: modelo base y estructura del repositorio"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/TU_REPOSITORIO.git
git push -u origin main
```

> El `git remote` se configura **una sola vez** y solo después de crear el repositorio remoto. Estos comandos no publican nada automáticamente en su cuenta; debe ejecutarlos con su propio acceso.

## Paso 4. Requisitos que revisará el profesor

- Notebook `Restart & Run All` sin errores; reproducibilidad por semilla `1000 + ID`.
- Muestra de 35.000, particiones 24.500/5.250/5.250 y 28 variables.
- Actividades 1 a 4 completas, incluidos análisis de segmentos y costos.
- Comparación contra DummyClassifier y ejemplo de Ridge con MAE.
- Preguntas de negocio redactadas personalmente con cifras de su muestra.
- JSON del ID correcto, commits y ausencia de CSV originales pesados.

**Limitaciones metodológicas:** se estudian solo pedidos entregados y los costos de R$ 8 y R$ 35 son didácticos. Accuracy sola no mide utilidad para detectar la minoría de entregas tardias.