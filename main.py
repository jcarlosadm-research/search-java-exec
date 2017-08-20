import sys
from config import *
from concurrent.futures import ThreadPoolExecutor
from search.java.exec.util import FolderManager
from search.java.exec.util import JsonInputFile
from search.java.exec.util import JsonProcessedUrls
from search.java.exec.util import GitUtil
from search.java.exec import Analyzer

# make folders
if not FolderManager.create_folder(RESULT_FOLDER) or \
	not FolderManager.create_folder(TEMP_REPOS_FOLDER):
	print("error to create result and repos folder")
	sys.exit()

# open json file and get urls
jsonInputFile = JsonInputFile(INPUT_JSON_FILE)
urls = jsonInputFile.get_urls()

# for each url not in db do clone(url)
jsonProcessedUrls = JsonProcessedUrls(PROCESSED_JSON_FILE)
for url in urls:
	if not jsonProcessedUrls.check_url(url):

		git_util = GitUtil(url)
		if git_util.clone(TEMP_REPOS_FOLDER):

			# TODO: delete results if exists (results/project)
			
			# get a list of java files in temporary folder
			javafiles = FolderManager.list_of_javafiles(git_util.path)
			
			# run a thread for each file (limited by number of threads)
			pool = ThreadPoolExecutor(max_workers = MAX_WORKERS)
			number = 0
			for javafile in javafiles:
				analyzer = Analyzer(javafile)
				pool.submit(analyzer.store_if_eligible, number)
				number += 1

			# wait all threads
			pool.shutdown(wait = True)
			
			jsonProcessedUrls.add_url(url)

		git_util.delete_local_repo()
