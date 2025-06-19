
from app2 import invertir_texto

def test_invertir_texto():
    assert invertir_texto("Hola") == "aloH"
    assert invertir_texto("12345") == "54321"
    assert invertir_texto("") == ""
