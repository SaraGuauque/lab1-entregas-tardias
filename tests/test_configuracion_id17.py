"""Verifica la individualizacion sin usar los CSV de Olist."""
from pathlib import Path
import re
import nbformat


def test_id17_en_notebook_oficial():
    path = Path(__file__).resolve().parents[1] / 'notebooks/S12_ML_Challenge.ipynb'
    nb = nbformat.read(path, as_version=4)
    celda = nb.cells[11].source
    assert re.search(r'^ID_ESTUDIANTE\s*=\s*17\s*$', celda, re.M)
    assert 'semilla = 1000 + ID_ESTUDIANTE' in celda
    assert len(nb.cells) == 32


def test_las_cuatro_actividades_implementadas():
    path = Path(__file__).resolve().parents[1] / 'notebooks/S12_ML_Challenge.ipynb'
    nb = nbformat.read(path, as_version=4)
    codigo = '\n'.join(c.source for c in nb.cells if c.cell_type == 'code')
    for simbolo in ('class_weight=opcion', 'average_precision_score', 'roc_auc_score',
                    'tabla_errores', 'costo_fp_fn = ', 'mean_absolute_error',
                    'Autoverificación superada.'):
        assert simbolo in codigo
