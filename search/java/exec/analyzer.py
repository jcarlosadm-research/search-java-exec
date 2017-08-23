import os
import subprocess
import shlex
from shutil import copyfile
from search.java.exec.util import FolderManager

class Analyzer:
	def __init__(self,project_folder,filenumber,filepath):
		self.project_folder = project_folder
		self.filenumber = filenumber
		self.filepath = filepath
		self.filename = os.path.basename(filepath)

	def store_if_eligible(self):

		#	copy file to results
		folder = os.path.join(self.project_folder,str(self.filenumber))
		FolderManager.create_folder(folder)
		copyfile(self.filepath,os.path.join(folder,self.filename))

		#	try to compile file
		cmd = 'javac ' + os.path.join(folder,self.filename)
		proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		stdout, stderr = proc.communicate()

		listOfClassFiles = FolderManager.list_of_files(folder,"class")

		if not listOfClassFiles:
			FolderManager.delete_folder_recursive(folder)
		else:
			for classFile in listOfClassFiles:
				os.remove(os.path.join(folder,classFile))
