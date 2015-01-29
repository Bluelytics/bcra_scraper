# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BcraItem(scrapy.Item):
    date = scrapy.Field()
    Reservas = scrapy.Field()
    Asistencia= scrapy.Field()
    BaseMonetaria = scrapy.Field()
    Circulacion = scrapy.Field()
    BilletesPublico = scrapy.Field()
    EfectivoFinanciero = scrapy.Field()
    DepositosBCRA = scrapy.Field()
    LEBAC = scrapy.Field()
    DepositosFinancieras = scrapy.Field()
    CuentasCorrientes = scrapy.Field()
    CajasAhorro = scrapy.Field()
    APlazo = scrapy.Field()
    CEDROS = scrapy.Field()
    OtrosDepositos = scrapy.Field()
    PrestamosAPrivados = scrapy.Field()
    TasasInteresEntrePrivadas = scrapy.Field()
    TasasInteres30Dias = scrapy.Field()
    BADLAR = scrapy.Field()
    TasasLebac = scrapy.Field()
    CambioRef = scrapy.Field()
    CER = scrapy.Field()
