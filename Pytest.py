from tarea1 import Min_May, findW, resta


def test_CasoExito():
    assert Min_May("hola") == "HOLA"
    assert findW("Obi_wan_kenobi") == "Se encontró la letra w"
    assert resta(30, 20) == 10


def test_EntradaIncorrecta():
    assert Min_May((0, 1)) == "ERROR: LAS ENTRADA NO ES DE TIPO STRING"
    assert findW(29) == "ERROR: LA ENTRADA NO ERA UN STRING"


def test_NoNatural():
    assert resta(4, 5) == "ERROR: LA RESTA DE LOS NÚMEROS ES NEGATIVA"
