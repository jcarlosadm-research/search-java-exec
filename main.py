import os
from git import Repo
import urllib.request
import urllib.error

REPO_FOLDER = "repos"

# open json file and get urls

# for each url not in db do clone(url)

### get a list of java files in temporary folder

### run a thread for each file (limited by number of threads)

##### analyze imports of each file. if file ok, put in results (if not exists)

### after all files, mark url done in db, and delete temp directory
