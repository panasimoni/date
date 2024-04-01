from __future__ import annotations


class Date:
    def __init__(self, day: int, month: int, year: int):
     
    def es_bisiesto(year):
     return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def validar_fecha(dia, mes, año):

         if año < 1900 or año > 2050:
        año = 1900
    
        if mes < 1 or mes > 12:
        mes = 1
    
    dias_por_mes = [31, 28 if not es_bisiesto(año) else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if dia < 1 or dia > dias_por_mes[mes - 1]:
        dia = 1
    
    return dia, mes, año

dia_corregido, mes_corregido, año_corregido = validar_fecha(dia, mes, año)
print(f"Fecha corregida: {dia_corregido}-{mes_corregido}-{año_corregido}")


def is_leap_year(year: int) -> bool:
        resultado = False

        if year % 4 == 0 and year % 100 != 0:
            resultado == True
        elif year % 400 == 0:
            resultado == True 

        return resultado

def days_in_month(month: int, year: int) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (self.is_leap_year)(year) and month == 2:
            return 29
        else:
            return days[month-1]

def get_delta_days(self) -> int:
        '''Número de días transcurridos desde el 1-1-1900 hasta la fecha'''
        days = 0
        if (days_in_year = 365):
            print("Un año tiene 365 dias")
        else:
            print("El año es bisiesto por tanto tiene 366 dias")

def weekday(self) -> int:
        '''Día de la semana de la fecha (0 para domingo, ..., 6 para sábado).'''
        ...

def is_weekend(self) -> bool:
        ...

def short_date(self) -> str:
        '''02/09/2003'''
        ...

def __str__(self):
        '''MARTES 2 DE SEPTIEMBRE DE 2003'''
        ...

def __add__(self, days: int) -> Date:
        '''Sumar un número de días a la fecha'''
        ...

def __sub__(self, other: Date | int) -> int | Date:
        '''Dos opciones:
        1) Restar una fecha a otra fecha -> Número de días
        2) Restar un número de días la fecha -> Nueva fecha'''
        ...

def __lt__(self, other) -> bool:
        ...

def __gt__(self, other) -> bool:
        ...

def __eq__(self, other) -> bool:
        ...



if __name__ == "__main__":
    pass