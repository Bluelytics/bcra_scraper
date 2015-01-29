# -*- coding: utf-8 -*-
import scrapy, datetime


from bcra.items import BcraItem

start_date = datetime.date(2010,1,1)
#start_date = datetime.date(2015,1,21)
end_date = datetime.datetime.now().date()

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)

def getIntVal(value):
    try:
        return int(value)
    except Exception:
        return None

class BcraSpiderSpider(scrapy.Spider):
    name = "bcra_spider"
    allowed_domains = ["bcra.gov.ar"]
    start_urls = [
        'http://www.bcra.gov.ar/estadis/es010000.asp?FechaCons=%s' % x.strftime("%d/%m/%Y") for x in daterange(start_date, end_date)]

    def parse(self, response):
        values = response.xpath('//td[@class="Celda_Borde_Centro"]/text()').extract()

        item = BcraItem()
        item['date'] = response.url.split('=')[1]
        item['Reservas'] = getIntVal(values[0])
        item['Asistencia'] = getIntVal(values[1])
        item['BaseMonetaria'] = getIntVal(values[2])
        item['Circulacion'] = getIntVal(values[3])
        item['BilletesPublico'] = getIntVal(values[4])
        item['EfectivoFinanciero'] = getIntVal(values[5])
        item['DepositosBCRA'] = getIntVal(values[6])
        item['LEBAC'] = getIntVal(values[7])
        item['DepositosFinancieras'] = getIntVal(values[8])
        item['CuentasCorrientes'] = getIntVal(values[9])
        item['CajasAhorro'] = getIntVal(values[10])
        item['APlazo'] = getIntVal(values[11])
        item['CEDROS'] = getIntVal(values[12])
        item['OtrosDepositos'] = getIntVal(values[13])
        item['PrestamosAPrivados'] = getIntVal(values[14])
        item['TasasInteresEntrePrivadas'] = getIntVal(values[15])
        item['TasasInteres30Dias'] = getIntVal(values[16])
        item['BADLAR'] = getIntVal(values[17])
        item['TasasLebac'] = getIntVal(values[18])
        item['CambioRef'] = getIntVal(values[19])
        item['CER'] = getIntVal(values[20])

        if item['Reservas'] != None:
            return item
        else:
            return None
