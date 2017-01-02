from datetime import datetime

ahora = datetime.now ()

anio_ahora = ahora.year
mes_ahora = ahora.month
dia_ahora = ahora.day
hora_ahora = ahora.hour
minuto_ahora = ahora.minute
segundo_ahora = ahora.second

print '%s/%s/%s %s:%s:%s' % (ahora.year, ahora.month, ahora.day, ahora.hour, ahora.minute, ahora.second)

