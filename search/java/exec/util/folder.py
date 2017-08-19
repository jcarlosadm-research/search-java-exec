import os
import shutil

class FolderManager:
	def create_folder(path_dir):
		if not os.path.exists(path_dir):
			try:
				os.makedirs(path_dir)
			except:
				return False
		return True

	def delete_folder_recursive(path_dir):
		if path_dir and os.path.exists(path_dir):
			try:
				shutil.rmtree(path_dir)
			except:
				return False
		
		return True