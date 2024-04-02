from __future__ import annotations


class Date:
    def __init__(self, day: int, month: int, year: int):
        '''Validar día, mes y año. Se comprobará si la fecha es correcta
        (entre el 1-1-1900 y el 31-12-2050); si el día no es correcto, lo pondrá a 1;
        si el mes no es correcto, lo pondrá a 1; y si el año no es correcto, lo pondrá a 1900.
        Ojo con los años bisiestos.
        El 1-1-1900 fue lunes.
        '''
        ...

    @staticmethod
    def is_leap_year(year: int) -> bool:
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


    @staticmethod
    def days_in_month(month: int, year: int) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if Date.is_leap_year(year) and month == 2:
            return 29
        else:
            return days[month-1]

    def get_delta_days(self) -> int:
        days = 0
        for y in range(1900, self.year):
            if self.is_leap_year(y):
                days += 366
            else:
                days += 365

        for m in range(1, self.month):
            days += self.days_in_month(m, self.year)

        days += self.day

        return days

    @property
    def weekday(self) -> int:
        d, m, H, S = self.day, (self.month + 9) % 12 + 3, self.year % 100, self.year // 100
        return ((d + 13*(m+1)//5 + H + H//4 + S//4 - 2*S) % 7 + 6) % 7

    @property
    def is_weekend(self) -> bool:
            return self.weekday >= 5


    @property
    def short_date(self) -> str:
            return f"{self.day}/{self.month}/{self.year}"

        

    def __str__(self):
      dias_semana = ['LUNES', 'MARTES', 'MIÉRCOLES', 'JUEVES', 'VIERNES', 'SÁBADO','DOMINGO',]
      meses = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE', 'NOVIEMBRE', 'DICIEMBRE']
      return f"{dias_semana[self.weekday]} {self.day} {meses[self.month - 1]} {self.year}"

    def __add__(self, days: int) -> Date:
        from datetime import datetime, timedelta
        return Date(* (datetime(self.year, self.month, self.day) + timedelta(days=days)).timetuple()[:3])
        ...

    def __sub__(self, other: Date | int) -> int | Date:
        '''Dos opciones:
        1) Restar una fecha a otra fecha -> Número de días
        2) Restar un número de días la fecha -> Nueva fecha'''
        ...

    def __lt__(self, other) -> bool:
        if not isinstance(other, Date):
            raise TypeError("La comparación solo es válida entre fechas")
        return self.get_delta_days() < other.get_delta_days()

    def __gt__(self, other) -> bool:
        if not isinstance(other, Date):
            raise TypeError("La comparación solo es válida entre fechas")
        return self.get_delta_days() > other.get_delta_days()

    def __eq__(self, other) -> bool:
         if not isinstance(other, Date):
            raise TypeError("La comparación solo es válida entre fechas")
         return self.get_delta_days() == other.get_delta_days()
