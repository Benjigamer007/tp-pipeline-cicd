from src.calculadora import sumar


def test_sumar_dos_numeros_positivos():
    assert sumar(2, 3) == 5


def test_sumar_un_numero_negativo():
    assert sumar(-2, 3) == 1


def test_sumar_ceros():
    assert sumar(0, 0) == 0
