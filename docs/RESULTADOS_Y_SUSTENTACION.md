# Guia de lectura de resultados - S12 - ID 17

Este documento ayuda a preparar la sustentacion despues de ejecutar el notebook con los CSV reales. Las cifras individuales se encuentran en `reports/S12_resultados_ID_17.json` y `reports/S12_analisis_ID_17.md`.

## Que explicar en clase

1. **Problema:** predecir si la fecha real de entrega superara la fecha prometida, usando datos conocidos al aprobar el pago.
2. **Individualizacion:** el ID 17 produce la semilla 1017, con muestra estratificada de 35.000 pedidos, 24.500 de train, 5.250 valid y 5.250 test (test no se utiliza en S12).
3. **Variables:** 24 numericas y 4 categoricas, sin datos futuros como fecha de entrega real, dias de entrega o reseñas.
4. **Referencia:** `DummyClassifier` es una comparacion minima, predice siempre la clase mayoritaria. Puede obtener alta Accuracy y detectar cero casos tardios.
5. **Modelos:** regresion logistica con `class_weight=None` o `balanced`, elegida por F1 en validacion y Recall como desempate.
6. **Metrica clave:** Recall mide cuantos pedidos realmente tardios identifica. Precision indica cuantas alertas emitidas son correctas. F1 equilibra ambos.
7. **Segmentos:** compare tasa de error y numero de pedidos por mes y estado del cliente. No saque conclusiones de grupos con muy pocos casos.
8. **Costos ilustrativos:** cada FP cuesta R$ 8 y cada FN R$ 35. El costo total es `8*FP + 35*FN`, no es un costo real estimado de Olist.
9. **Regresion:** Ridge estima dias de entrega; MAE mide los dias promedio de error absoluto.
10. **Limitaciones y siguientes pasos:** solo se analizan pedidos ya entregados; muestreo aleatorio no es validacion temporal. En S13 se evaluara regularizacion/agrupacion de categorias manteniendo muestra y particiones.

## Antes de entregar

- Lea `reports/S12_analisis_ID_17.md` y revise personalmente los tres apartados de interpretacion.
- Confirme que las cifras mencionadas en el notebook coincidan con el JSON.
- Ejecute `python scripts/verificar_entrega.py` o compruebe la ejecucion exitosa del flujo GitHub Actions.
- No copie conclusiones ni resultados de los repositorios enviados como ejemplos.