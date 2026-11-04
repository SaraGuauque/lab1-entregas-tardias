"""Ejecuta S12 con ID oficial y actualiza notebook y evidencias reproducibles."""
import argparse
from pathlib import Path
import re
import sys

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
NB_PATH = ROOT / 'notebooks' / 'S12_ML_Challenge.ipynb'


def ejecutar(id_estudiante):
    if not (1 <= id_estudiante <= 30):
        raise ValueError('El ID debe estar entre 1 y 30 y debe ser el oficial.')
    notebook = nbformat.read(NB_PATH, as_version=4)
    indice = next((i for i, celda in enumerate(notebook.cells)
                   if celda.cell_type == 'code' and 'ID_ESTUDIANTE =' in celda.source), None)
    if indice is None:
        raise RuntimeError('No se encontro la celda ID_ESTUDIANTE.')
    original = notebook.cells[indice].source
    actual = re.search(r'^ID_ESTUDIANTE\s*=\s*(None|\d+)\s*$', original, flags=re.MULTILINE)
    if not actual:
        raise RuntimeError('La asignacion del ID tiene un formato inesperado.')
    notebook.cells[indice].source = re.sub(
        r'^ID_ESTUDIANTE\s*=\s*(None|\d+)\s*$',
        f'ID_ESTUDIANTE = {id_estudiante}', original, count=1, flags=re.MULTILINE)
    for celda in notebook.cells:
        if celda.cell_type == 'code':
            celda.execution_count = None
            celda.outputs = []
    print(f'Ejecutando S12 con ID oficial {id_estudiante:02d}...', flush=True)
    client = NotebookClient(notebook, timeout=900, kernel_name='python3',
                            resources={'metadata': {'path': str(ROOT)}},
                            allow_errors=False)
    client.execute()
    nombre = f'{id_estudiante:02d}'
    ruta_analisis = ROOT / 'reports' / f'S12_analisis_ID_{nombre}.md'
    if not ruta_analisis.exists():
        raise RuntimeError('El notebook termino sin generar el analisis esperado.')
    # Mantener las respuestas redactadas y sustentadas por la estudiante.
    # El análisis automático se genera como reporte aparte, sin sobrescribirlas.
    nbformat.validate(notebook)
    nbformat.write(notebook, NB_PATH)
    print(f'Listo: {NB_PATH.relative_to(ROOT)}', flush=True)
    print(f'JSON: reports/S12_resultados_ID_{nombre}.json', flush=True)
    print('Revise/redacte sus interpretaciones y luego haga commit en GitHub.', flush=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ejecuta el reto S12 con el ID verdadero.')
    parser.add_argument('--id', type=int, required=True, dest='identificador',
                        help='identificador individual (para Sara: 17)')
    args = parser.parse_args()
    try:
        ejecutar(args.identificador)
    except Exception as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        raise
