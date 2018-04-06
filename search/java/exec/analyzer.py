import os
import subprocess
import shlex
from shutil import copyfile
from search.java.exec.util import FolderManager
from search.java.exec.ast import JavaAst
from colorama import Fore
from colorama import Style

class Analyzer:
    def __init__(self,project_folder,filenumber,filepath):
        self.project_folder = project_folder
        self.filenumber = filenumber
        self.filepath = filepath
        self.filename = os.path.basename(filepath)

    def store_if_eligible(self):
        print("   analyzing " + self.filepath)

        #    copy file to results
        folder = os.path.join(self.project_folder,str(self.filenumber))
        FolderManager.create_folder(folder)
        copyfile(self.filepath,os.path.join(folder,self.filename))

        #    try to compile file
        cmd = 'javac ' + os.path.join(folder,self.filename)
        print("   compiling " + os.path.join(folder,self.filename))
        proc = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = proc.communicate()

        listOfClassFiles = FolderManager.list_of_files(folder,"class")

        print("   file " + os.path.join(folder, self.filename),end="")
        if not listOfClassFiles:
            FolderManager.delete_folder_recursive(folder)
            print(f': {Fore.RED}not OK{Style.RESET_ALL}')
        else:
            for classFile in listOfClassFiles:
                os.remove(os.path.join(folder,classFile))

            javaAst = JavaAst(os.path.join(folder,self.filename))
            if not javaAst.is_valid():
                FolderManager.delete_folder_recursive(folder)
                print(f': {Fore.RED}not OK{Style.RESET_ALL}')
            else:
                print(f': {Fore.GREEN}OK{Style.RESET_ALL}')
