"""Verifica que los resultados correspondan a la muestra Olist ID 17."""
from pathlib import Path
import json
import math
import sys

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / 'reports' / 'S12_resultados_ID_17.json'


def verificar():
    if not REPORT.is_file():
        raise FileNotFoundError(
            'No existe reports/S12_resultados_ID_17.json. '
            'Ejecute el notebook con Olist antes de validar la entrega.')
    d = json.loads(REPORT.read_text(encoding='utf-8'))
    esperados = {
        'laboratorio': 'S12', 'id_estudiante': '17', 'semilla': 1017,
        'n_muestra': 35000, 'n_train': 24500, 'n_valid': 5250,
        'n_test': 5250, 'n_variables': 28,
        'fuente_olist_commit': 'fa0cc6d1aff713d3c8b9a1e633b56889881848bf',
    }
    for clave, valor in esperados.items():
        if d.get(clave) != valor:
            raise AssertionError(f'{clave}: se esperaba {valor!r}, se obtuvo {d.get(clave)!r}')
    if len(d.get('columnas_predictoras', [])) != 28:
        raise AssertionError('Faltan variables predictoras.')
    if not isinstance(d.get('huella_muestra'), str) or len(d['huella_muestra']) != 12:
        raise AssertionError('Huella de la muestra invalida.')
    metrics = d.get('metricas', {})
    for name in ('accuracy', 'precision', 'recall', 'f1', 'roc_auc', 'ap'):
        value = metrics.get(name)
        if not isinstance(value, (int, float)) or not math.isfinite(value) or not 0 <= value <= 1:
            raise AssertionError(f'Metrica de validacion invalida: {name}={value!r}')
    matriz = d.get('matriz_confusion_validacion', [])
    if len(matriz) != 2 or any(len(r) != 2 for r in matriz):
        raise AssertionError('Matriz de confusion faltante o invalida.')
    if sum(sum(r) for r in matriz) != 5250:
        raise AssertionError('La matriz de confusion no suma 5.250 pedidos.')
    if d['costo_errores_brl'] != 8*matriz[0][1] + 35*matriz[1][0]:
        raise AssertionError('Costo calculado no coincide con FP/FN.')
    otros = [
        ROOT / 'reports' / 'S12_errores_mes_ID_17.csv',
        ROOT / 'reports' / 'S12_errores_estado_ID_17.csv',
        ROOT / 'reports' / 'S12_analisis_ID_17.md',
        ROOT / 'reports' / 'figuras' / 'S12_matriz_ID_17.png',
        ROOT / 'reports' / 'figuras' / 'S12_segmentos_ID_17.png',
    ]
    for path in otros:
        if not path.is_file() or path.stat().st_size == 0:
            raise AssertionError(f'Falta una evidencia: {path.relative_to(ROOT)}')
    import nbformat
    nb = nbformat.read(ROOT / 'notebooks' / 'S12_ML_Challenge.ipynb', as_version=4)
    code = [c for c in nb.cells if c.cell_type == 'code']
    if not all(c.execution_count is not None for c in code):
        raise AssertionError('El notebook no esta ejecutado de principio a fin.')
    if any(any(getattr(o, 'output_type', '') == 'error' for o in c.outputs) for c in code):
        raise AssertionError('El notebook contiene errores de ejecucion.')
    if 'ID_ESTUDIANTE = 17' not in nb.cells[11].source:
        raise AssertionError('El notebook no esta configurado para el ID 17.')
    print('OK: ID 17, semilla 1017, 35.000 pedidos, 28 predictores y todas las evidencias verificadas.')
    return d


if __name__ == '__main__':
    try:
        verificar()
    except Exception as exc:
        print(f'VALIDACION FALLIDA: {exc}', file=sys.stderr)
        raise
