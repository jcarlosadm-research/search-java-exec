

class Analyzer:
	def __init__(self,filepath):
		self.filepath = filepath

	def store_if_eligible(self,fileNumber):
		# TODO: analyze imports of file. if file ok, put in results (if not exists)

		# file is ok
		# open file
		# line by line:
		#	if contains import:
		#		check: if import is not default library, halt and file is not ok
		# if file ok:
		#	copy file to results (results/project/file+fileNumber(four digits format)/file.java)
		#	try to compile file
		#	if not compile:
		#		delete folder (results/project/file+fileNumber(four digits format))
		pass