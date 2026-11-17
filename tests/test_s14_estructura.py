"""Comprobaciones estáticas del nuevo laboratorio sin datos externos."""
from pathlib import Path
import nbformat

RAIZ = Path(__file__).resolve().parents[1]
RUTA = RAIZ / "notebooks" / "S14_Lab2_PCA_Validacion_ID_17.ipynb"


def test_s14_id_particion_y_huella():
    nb = nbformat.read(RUTA, as_version=4)
    codigo = "\n".join(c.source for c in nb.cells if c.cell_type == "code")
    assert "ID_ESTUDIANTE = 17" in codigo
    assert "semilla = 1000 + ID_ESTUDIANTE" in codigo
    assert "'55ced66ce4f4'" in codigo
    assert "train_size=35000" in codigo
    assert "test_size=0.30" in codigo
    assert "test_size=0.50" in codigo
    assert "X_test" not in codigo


def test_s14_pca_y_comparacion_controlada():
    nb = nbformat.read(RUTA, as_version=4)
    codigo = "\n".join(c.source for c in nb.cells if c.cell_type == "code")
    for exigencia in (
        "PCA(n_components=0.90", "svd_solver='full'", "StandardScaler()",
        "class_weight='balanced'", "('A_sin_PCA_C1', False, 1.0)",
        "('B_PCA90_C1', True, 1.0)",
        "('C_PCA90_C0_1', True, 0.1)",
        "('D_PCA90_C10', True, 10.0)",
        "ks_2samp(", "'valor_flete'", "costo_brl",
        "S14_resultados_ID_17.json", "S14_experimentos_ID_17.csv",
    ):
        assert exigencia in codigo, exigencia
