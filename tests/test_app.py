from app import generar_frases_desde_csv
import os

def test_generar_frases():
    # Preparamos un archivo temporal con frases de prueba
    archivo = "test_frases.csv"
    with open(archivo, "w", encoding="utf-8") as f:
        f.write("Frase\n")
        f.write("Hasta el infinito y más allá\n")
        f.write("Yo soy tu padre\n")

    resultado = generar_frases_desde_csv(archivo)

    # El resultado debería contener texto generado (no vacío)
    assert isinstance(resultado, str)
    assert len(resultado.strip()) > 0

    # Limpiar archivo temporal
    os.remove(archivo)
