"""Comprueba tamaño, muestra, cuatro modelos, PCA, KS, costos y evidencias S14."""
from pathlib import Path
import json
import math
import pandas as pd
import nbformat

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "S14_resultados_ID_17.json"
NOTEBOOK = ROOT / "notebooks" / "S14_Lab2_PCA_Validacion_ID_17.ipynb"


def verificar():
    d = json.loads(REPORT.read_text(encoding="utf-8"))
    expected = {
        "laboratorio": "S14_Lab2", "id_estudiante": "17",
        "semilla": 1017, "huella_muestra": "55ced66ce4f4",
        "n_muestra": 35000, "n_train": 24500,
        "n_valid": 5250, "n_test_reservado": 5250,
        "n_variables_originales": 28, "n_numericas": 24,
        "n_categoricas": 4, "umbral": 0.5,
        "class_weight": "balanced", "costo_fp_brl": 8, "costo_fn_brl": 35,
    }
    for clave, valor in expected.items():
        assert d.get(clave) == valor, f"{clave}: esperado {valor!r}; recibido {d.get(clave)!r}"
    n = d["n_componentes_pca_90"]
    assert isinstance(n, int) and 1 <= n <= 24
    assert 0.9 <= d["varianza_retenida"] <= 1.0
    cfgs = d["configuraciones"]
    assert len(cfgs) == 4 and {c["modelo"] for c in cfgs} == {
        "A_sin_PCA_C1", "B_PCA90_C1", "C_PCA90_C0_1", "D_PCA90_C10"}
    for c in cfgs:
        for key in ("accuracy","precision","recall","f1","ap","roc_auc"):
            assert math.isfinite(c[key]) and 0 <= c[key] <= 1, f"{c['modelo']}: {key}"
        assert c["umbral"] == 0.5 and c["class_weight"] == "balanced"
        assert c["tn"] + c["fp"] + c["fn"] + c["tp"] == 5250
        assert c["costo_brl"] == c["fp"]*8 + c["fn"]*35
    assert d["modelo_menor_costo"] == min(
        cfgs, key=lambda c: (c["costo_brl"],-c["f1"],-c["recall"]))["modelo"]
    ks = d["ks"]
    assert ks["variable"] == "valor_flete"
    assert ks["alfa"] == 0.05
    assert 0 <= ks["estadistico_d"] <= 1 and 0 <= ks["pvalue"] <= 1
    assert ks["rechaza_h0"] == (ks["pvalue"] < ks["alfa"])
    assert ks["n_train"] == 24500 and ks["n_valid"] == 5250

    csv = pd.read_csv(ROOT / "reports" / "S14_experimentos_ID_17.csv")
    assert len(csv) == 4 and set(csv["modelo"]) == {c["modelo"] for c in cfgs}
    for name in (
        "reports/S14_analisis_ID_17.md",
        "reports/figuras/S14_pca_varianza_ID_17.png",
        "reports/figuras/S14_comparacion_modelos_ID_17.png",
        "reports/figuras/S14_ks_flete_ID_17.png",
    ):
        path = ROOT / name
        assert path.is_file() and path.stat().st_size > 0, f"Falta archivo: {name}"
    texto = (ROOT / "reports/S14_analisis_ID_17.md").read_text(encoding="utf-8")
    assert "## PCA" in texto and "## Cuatro modelos" in texto and "## Prueba KS" in texto

    nb = nbformat.read(NOTEBOOK, as_version=4)
    celdas = [c for c in nb.cells if c.cell_type == "code"]
    assert len(celdas) >= 12
    assert all(isinstance(c.execution_count,int) for c in celdas)
    assert not any(o.output_type == "error" for c in celdas for o in c.outputs)
    assert all("borrador" not in str(c.source).lower() for c in nb.cells)
    print(f"OK S14 ID 17: PCA {n} componentes; 4 modelos; "
          f"KS D={ks['estadistico_d']:.4f}, p={ks['pvalue']:.5g}; "
          f"elección {d['modelo_menor_costo']}.")
    return d


if __name__ == "__main__":
    verificar()
