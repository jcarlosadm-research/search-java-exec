import os
from git import Repo
import urllib.request
import urllib.error
import shutil

class GitUtil:
	def __init__(self,url):
		self.url = url
		self.foldername = self.build_foldername()
		self.path = ""
	
	def build_foldername(self):
		basename = self.url
		
		index = basename.rfind('/') + 1;
		if index != -1:
			basename = self.url[index:]
		
		index = basename.find('.');
		if index != -1:
			basename = basename[:index]
		
		return basename
	
	def clone(self,repos_folder):
		try:
			req = urllib.request.Request(self.url)
			urllib.request.urlopen(req)
			Repo.clone_from(self.url, os.path.join(repos_folder,self.foldername))
			self.path = os.path.join(repos_folder,self.foldername)
			return True
		except urllib.error.HTTPError:
			return False
	
	def delete_local_repo(self):
		if self.path and os.path.exists(self.path):
			try:
				shutil.rmtree(self.path)
			except:
				return False
		
		return True
