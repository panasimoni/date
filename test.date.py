from date import Date

fecha = Date(14, 9, 2022)

fecha2 = Date(31, 12, 2023)

def test__add():
    nueva_fecha = fecha1 + 11
    assert str(nueva_fecha) == "LUNES 11 ENERO 2023"

def test_date():
    diferencia = fecha1 - fecha2
    assert diferencia == 365

def test_lt():
    assert fecha1 < fecha2

def test_gt():
    assert fecha2 > fecha1

def test_eq():
    assert fecha1 == fecha1