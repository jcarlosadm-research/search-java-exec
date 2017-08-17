import json

class JsonInputFile:
	def __init__(self, path):
		self.path = path

	def get_urls(self):
		validurl = []
		with open(self.path) as data_file:
			data = json.load(data_file)

		for item in data:
			value = ""
			try:
				value = item['url']
				if value and value not in validurl:
					validurl.append(value)
			except:
				pass

		return validurl
