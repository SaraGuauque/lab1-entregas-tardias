"""Pruebas locales. No utilizan ni inventan datos reales de Olist."""
import pandas as pd
import pytest
from src.evaluacion import costo_por_confusion, errores_por_segmento, huella_pedidos


def test_huella_estable_independiente_del_orden():
    assert huella_pedidos(['b','a','c']) == huella_pedidos(['c','b','a'])
    assert len(huella_pedidos(['a'])) == 12


def test_costo_ponderado_falsos_positivos_y_negativos():
    true = [0, 0, 1, 1]
    pred = [0, 1, 0, 1]
    resultado = costo_por_confusion(true, pred)
    assert resultado == {
        'tn': 1, 'fp': 1, 'fn': 1, 'tp': 1,
        'costo_fp': 8, 'costo_fn': 35, 'total': 43}


def test_grupos_suman_observaciones_y_costos():
    tabla = pd.DataFrame({
        'mes': [1, 1, 2, 2], 'is_late': [0, 0, 1, 1], 'pred': [1, 0, 0, 1]})
    resumen = errores_por_segmento(tabla, 'mes')
    assert resumen['total_pedidos'].sum() == 4
    assert resumen['pedidos_erroneos'].sum() == 2
    assert resumen['costo_brl'].sum() == 43
    assert resumen.set_index('mes').loc[1, 'tasa_error_pct'] == 50


def test_error_de_entrada_que_falta():
    with pytest.raises(ValueError, match='Faltan columnas'):
        errores_por_segmento(pd.DataFrame({'mes': [1]}), 'mes')
