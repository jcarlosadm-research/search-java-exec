import json

class JsonInputFile:
	def __init__(self, path):
		self.path = path

	def get_urls(self):
		data = []

		try:
			with open(self.path) as f:
				data = json.load(f)
		except:
			pass

		return data

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

class JsonMaker:
	@staticmethod
	def list_to_json(filepath, url_list):
		with open(filepath,'w') as f:
			json.dump(url_list, f)