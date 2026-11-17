"""Ejecuta la semana 14 con Olist real y guarda el notebook en GitHub."""
from pathlib import Path
import sys

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "notebooks" / "S14_Lab2_PCA_Validacion_ID_17.ipynb"
INFORME = ROOT / "reports" / "S14_analisis_ID_17.md"


def ejecutar():
    nb = nbformat.read(NOTEBOOK, as_version=4)
    for cell in nb.cells:
        if cell.cell_type == "code":
            cell.execution_count = None
            cell.outputs = []

    print("Ejecutando laboratorio S14: ID 17, semilla 1017, datos reales de Olist.",
          flush=True)
    client = NotebookClient(
        nb, timeout=1200, kernel_name="python3",
        resources={"metadata": {"path": str(ROOT)}}, allow_errors=False,
    )
    client.execute()

    if not INFORME.is_file():
        raise RuntimeError("No se generó el informe S14. Revisa la última celda.")
    contenido = INFORME.read_text(encoding="utf-8")
    # Se completa la sección final solo si aún muestra el texto introductorio.
    # Si existen conclusiones personales posteriores, no se sobrescriben.
    for cell in nb.cells:
        if cell.cell_type == "markdown" and "Los resultados cuantitativos y las conclusiones se registran" in cell.source:
            cell.source = "### Resultados individuales del laboratorio S14\n\n" + contenido
            break

    nbformat.validate(nb)
    nbformat.write(nb, NOTEBOOK)
    print("Notebook S14 ejecutado y publicado con las figuras y métricas.")
    print("Evidencias: reports/S14_* y reports/figuras/S14_*")


if __name__ == "__main__":
    try:
        ejecutar()
    except Exception as error:
        print("Error durante la ejecución S14:", error, file=sys.stderr)
        raise
