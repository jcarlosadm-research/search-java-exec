import json

class JsonInputFile:
	def __init__(self, path):
		self.path = path

	def get_urls(self):
		validurls = []
		data = []
		try:
			with open(self.path) as data_file:
				data = json.load(data_file)
		except:
			pass

		for item in data:
			value = ""
			try:
				value = item['url']
				if value and value not in validurls:
					validurls.append(value)
			except:
				pass

		return validurls

class JsonProcessedUrls:
	def __init__(self, path):
		self.path = path
	
	def check_url(self, url):
		data = []
		try:
			with open(self.path) as data_file:
				data = json.load(data_file)
		except:
			pass
		
		return url in data
	
	def add_url(self, url):
		data = []
		try:
			with open(self.path) as data_file:
				data = json.load(data_file)
		except:
			pass
		
		if url not in data:
			data.append(url)
			
			with open(self.path, 'w') as outfile:
				json.dump(data, outfile)
