import os
import unittest
from search.java.exec import Analyzer
from search.java.exec.util import FolderManager

REPO_TEST = os.path.join("tests","resources","JavaPatternFinder")
RESULT_FOLDER = os.path.join("tests","temp_project_analyzer")

class AnalyzerTest(unittest.TestCase):
	def test_store_if_eligible(self):
		java_files = FolderManager.list_of_javafiles(REPO_TEST)
		
		FolderManager.create_folder(RESULT_FOLDER)
		
		list_to_check = []
		
		index = 0
		for java_file in java_files:
			if os.path.basename(java_file) == "PropertiesManager.java" or \
			os.path.basename(java_file) == "Folders.java":
				list_to_check.append(os.path.join(RESULT_FOLDER,str(index), \
				os.path.basename(java_file)))
			
			analyzer = Analyzer(RESULT_FOLDER,index,java_file)
			analyzer.store_if_eligible()
			
			index += 1
		
		java_files = FolderManager.list_of_javafiles(RESULT_FOLDER)
		
		for file_to_check in list_to_check:
			self.assertTrue(file_to_check in java_files)
		
		self.assertEqual(len(java_files),len(list_to_check))
		
		FolderManager.delete_folder_recursive(RESULT_FOLDER)
