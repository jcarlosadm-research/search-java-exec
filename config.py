import os

# Folders
RESULT_FOLDER = "results"
TEMP_REPOS_FOLDER = "repos"

# files
INPUT_JSON_FILE = "github_search.json"
PROCESSED_JSON_FILE = os.path.join(RESULT_FOLDER,"processed_urls.json")

# threading
MAX_WORKERS = 1

# github token file
GITHUB_TOKEN_FILE = "token"

# github search repository
GITHUB_SEARCH_REPO_QUERY = ""
GITHUB_SEARCH_REPO_SORT = "stars"
GITHUB_SEARCH_REPO_ORDER = "desc"
GITHUB_SEARCH_REPO_LANGUAGE = "Java"
GITHUB_SEARCH_HAS_FORK = "false"
GITHUB_SEARCH_REPO_GENFILE = "github_search.json"
GITHUB_SEARCH_REPO_MAXRESULT = 1000