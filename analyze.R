library(RJSONIO)
library(forecast)
library(lubridate)

data <- fromJSON('initial.json')

parseCol <- function(col){
  
  filterCol <- function(val){
    return (c(val$date, val[col]))
  }
  filtered <- lapply(data, filterCol)
  DF <- do.call(rbind.data.frame, filtered)
  colnames(DF) <- c('date', 'x')
  DF$date <- as.Date(DF$date, format="%d/%m/%Y")
  return (DF)
  
}

convertTs <- function(serie){  
  serie <- subset(serie, x>0)
  days <- data.frame ( date = as.Date(seq.POSIXt(ymd(min(serie$date)), ymd(max(serie$date)), by = "1 day")))
  
  
  final <- na.locf(merge(days, serie, by="date", all.x=TRUE))
  final$x <- as.numeric(final$x)
  
  
  finaldate = min(ymd(final$date))
  
  myts <- ts(final$x, start=c(year(finaldate), yday(finaldate)), frequency=365)
  return (myts) 
}
  
procesar <- function(name){
  columna <- parseCol(name)
  bts <- convertTs(columna)
  plot(bts, ylab=name, main=name)
  
  days <- seq(min(columna$date), by='day', length.out=length(bts))
  
  resultado <- data.frame(date=days, x=bts)
  
  write.csv(resultado, paste('out/', name, '.csv', sep=""))
  
}

procesar('Reservas')
procesar('Asistencia')
procesar('BaseMonetaria')
procesar('Circulacion')
procesar('BilletesPublico')
procesar('EfectivoFinanciero')
procesar('DepositosBCRA')
procesar('LEBAC')
procesar('DepositosFinancieras')
procesar('CuentasCorrientes')
procesar('CajasAhorro')
procesar('APlazo')
procesar('OtrosDepositos')
procesar('PrestamosAPrivados')
procesar('TasasInteresEntrePrivadas')
procesar('TasasInteres30Dias')
procesar('BADLAR')
procesar('CambioRef')
procesar('CER')
