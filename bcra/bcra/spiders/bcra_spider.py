# -*- coding: utf-8 -*-
import scrapy
from datetime import datetime, date, timedelta

from bcra.items import BcraItem

end_date = datetime.now().date()
start_date = end_date - timedelta(days=200)
#start_date = date(2010,1,1)

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def getFloatVal(value):
    try:
        return float(value.replace(',','.'))
    except Exception:
        return None

class BcraSpiderSpider(scrapy.Spider):
    name = "bcra_spider"
    allowed_domains = ["bcra.gov.ar"]
    start_urls = [
        'http://www.bcra.gov.ar/PublicacionesEstadisticas/Principales_variables.asp?FechaCons=%s' % x.strftime("%d/%m/%Y") for x in daterange(start_date, end_date)]

    def parse(self, response):
        values = response.xpath('//table[@class="table table-BCRA table-bordered table-responsive table-hover"]/tbody/tr/td[@style="text-align:right"]/text()').extract()

        item = BcraItem()

        item['date'] = response.url.split('=')[1]
        item['CEDROS'] = 0
        item['Asistencia'] = 0
        item['UVA'] = getFloatVal(values[0])
        item['Reservas'] = getFloatVal(values[1])
        item['BaseMonetaria'] = getFloatVal(values[2])
        item['Circulacion'] = getFloatVal(values[3])
        item['BilletesPublico'] = getFloatVal(values[4])
        item['EfectivoFinanciero'] = getFloatVal(values[5])
        item['DepositosBCRA'] = getFloatVal(values[6])
        item['LEBAC'] = getFloatVal(values[7])
        item['LEBACNominal'] = getFloatVal(values[8])
        item['DepositosFinancieras'] = getFloatVal(values[9])
        item['CuentasCorrientes'] = getFloatVal(values[10])
        item['CajasAhorro'] = getFloatVal(values[11])
        item['APlazo'] = getFloatVal(values[12])
        item['OtrosDepositos'] = getFloatVal(values[13])
        item['TasasLebac'] = getFloatVal(values[14])
        item['TasasInteresPaseActivas'] = getFloatVal(values[15])
        item['TasasInteresPasePasivas'] = getFloatVal(values[16])
        item['PrestamosAPrivados'] = getFloatVal(values[17])
        item['TasasInteresEntrePrivadas'] = getFloatVal(values[18])
        item['TasasInteres30Dias'] = getFloatVal(values[19])
        item['BADLAR'] = getFloatVal(values[20])
        item['CambioRef'] = getFloatVal(values[21])
        item['CER'] = getFloatVal(values[22])

        if item['Reservas'] != None:
            return item
        else:
            raise Exception("No data on date " + item['date'])
