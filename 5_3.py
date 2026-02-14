class Date:
    def __init__(self, dia, mes, anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio

    def rellenar_ceros(self, numero, cantidad):
        texto = str(numero)

        while len(texto) < cantidad:
            texto = "0" + texto

        return texto

    def __str__(self):
        dia_formato = self.rellenar_ceros(self.dia, 2)
        mes_formato = self.rellenar_ceros(self.mes, 2)
        anio_formato = self.rellenar_ceros(self.anio, 4)

        return dia_formato + " / " + mes_formato + " / " + anio_formato

fecha1 = Date(8, 7, 1998)
print(fecha1)

fecha2 = Date(3, 2, 9)
print(fecha2)
