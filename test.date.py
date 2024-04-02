from date import Date

fecha = Date(14, 9, 2022)

fecha2 = Date(31, 12, 2023)

def test__add():
    nueva_fecha = fecha1 + 11
    assert str(nueva_fecha) == "LUNES 11 ENERO 2023"

def test_date():
    diferencia = fecha1 - fecha2
    assert diferencia == 365

