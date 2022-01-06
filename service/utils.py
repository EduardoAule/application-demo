# Import datetime module
import datetime as dt
# Import pyzt module
import pytz
import time

class Utils():
	def __init__(self):
		pass
	
	def set_dt_expiration(self):
		newTimeZone = pytz.timezone('America/Mexico_City')
		fecha_actual = dt.datetime.now(tz=newTimeZone)
		# Set the date and time format
		dt_format = "%Y-%d-%m/%H:%M"
		print('=>Datetime of UTC Time-zone: ', fecha_actual.strftime(dt_format))
		fecha_actual = fecha_actual + dt.timedelta(minutes=5)
		print('=>Datetime of UTC Time-zone + 5 min: ', fecha_actual.strftime(dt_format))
		return fecha_actual.strftime(dt_format)

	def validate(self, data):
		data_buf = data.split("@")
		data_datetime = data_buf[1].split("/")
		print(data_datetime)
		# obtener la fecha-hora actual de la zona horaria
		newTimeZone = pytz.timezone('America/Mexico_City')
		fecha_actual = dt.datetime.now(tz=newTimeZone)
		# Set the date and time format
		dt_format = "%Y-%d-%m %H:%M"
		fecha_actual_local = fecha_actual.strftime(dt_format)
		print('=>LocalDatetime of UTC Time-zone: ', fecha_actual_local)

		fecha_qr = data_datetime[0] + " " + data_datetime[1]
		print("fecha_actual_local:", fecha_actual_local)
		print("fecha_qr:", fecha_qr)
		# comparando fechas
		formatted_date1 = time.strptime(fecha_actual_local, "%Y-%d-%m %H:%M")
		formatted_date2 = time.strptime(fecha_qr, "%Y-%d-%m %H:%M")
		print(formatted_date1 > formatted_date2)
		print(formatted_date1 < formatted_date2)
		return formatted_date1 < formatted_date2