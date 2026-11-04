"""Metodos de evaluacion sin acceso al conjunto de prueba reservado."""

from hashlib import sha256
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix


def huella_pedidos(order_ids):
    """Crea la misma huella de 12 caracteres empleada en el notebook oficial."""
    ids = sorted(str(pedido) for pedido in order_ids)
    return sha256('|'.join(ids).encode('utf-8')).hexdigest()[:12]


def costo_por_confusion(y_true, y_pred, costo_fp=8, costo_fn=35):
    """Devuelve los cuatro cuadrantes y el costo de la validacion."""
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()
    return {
        'tn': int(tn), 'fp': int(fp), 'fn': int(fn), 'tp': int(tp),
        'costo_fp': int(fp) * costo_fp,
        'costo_fn': int(fn) * costo_fn,
        'total': int(fp) * costo_fp + int(fn) * costo_fn,
    }


def errores_por_segmento(tabla, segmento):
    """Agrupa n, errores, FP, FN y tasa por segmento sin filtrar casos raros."""
    requeridas = {segmento, 'is_late', 'pred'}
    if not requeridas.issubset(tabla.columns):
        raise ValueError(f'Faltan columnas: {sorted(requeridas - set(tabla.columns))}')
    base = tabla.copy()
    base['error'] = base['is_late'].ne(base['pred']).astype(int)
    base['fp'] = base['is_late'].eq(0).mul(base['pred'].eq(1)).astype(int)
    base['fn'] = base['is_late'].eq(1).mul(base['pred'].eq(0)).astype(int)
    resultado = (base.groupby(segmento, dropna=False)
                 .agg(total_pedidos=('error', 'size'),
                      pedidos_erroneos=('error', 'sum'),
                      falsos_positivos=('fp', 'sum'),
                      falsos_negativos=('fn', 'sum'))
                 .reset_index())
    resultado['tasa_error_pct'] = 100 * resultado['pedidos_erroneos'] / resultado['total_pedidos']
    resultado['costo_brl'] = 8 * resultado['falsos_positivos'] + 35 * resultado['falsos_negativos']
    return resultado
