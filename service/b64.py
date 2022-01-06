import base64

class B64():
	def __init__(self):
		pass
	def encode(self, message):

		message_bytes = message.encode('ascii')
		base64_bytes = base64.b64encode(message_bytes)
		base64_message = base64_bytes.decode('ascii')
		# print(base64_message)
		return base64_message

	def decode(self, base64_message):
		# base64_message = 'UHl0aG9uIGlzIGZ1bg=='
		base64_bytes = base64_message.encode('ascii')
		message_bytes = base64.b64decode(base64_bytes)
		message = message_bytes.decode('ascii')
		# print(message)
		return message