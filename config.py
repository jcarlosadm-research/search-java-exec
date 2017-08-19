import os

# Folders

RESULT_FOLDER = "results"
TEMP_REPOS_FOLDER = "repos"

# files

INPUT_JSON_FILE = "repositories.json"
PROCESSED_JSON_FILE = os.path.join(RESULT_FOLDER,"processed_urls.json")

# threading

MAX_WORKERS = 3