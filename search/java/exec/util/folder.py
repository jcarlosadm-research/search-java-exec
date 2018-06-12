import os
import glob
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

    def list_of_files(path_dir,extension):
        files = []
        try:
            for file in os.listdir(path_dir):
                if file.endswith("." + extension):
                    files.append(file)
        except:
            pass

        return files

    def list_of_javafiles(path_dir):
        files = []
        try:
            for dirpath, dirnames, filenames in os.walk(path_dir):
                for filename in [f for f in filenames if f.endswith(".java")]:
                    files.append(os.path.join(dirpath, filename))
        except:
            pass

        return files
