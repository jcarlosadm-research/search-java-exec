from config import GITHUB_TOKEN_FILE
from config import GITHUB_SEARCH_REPO_GENFILE
from config import GITHUB_SEARCH_REPO_QUERY
from config import GITHUB_SEARCH_REPO_SORT
from config import GITHUB_SEARCH_REPO_ORDER
from config import GITHUB_SEARCH_REPO_LANGUAGE
from config import GITHUB_SEARCH_HAS_FORK
from config import GITHUB_SEARCH_REPO_MAXRESULT
from search.java.exec.util import JsonMaker
from search.java.exec.util import GithubSearch

# get token file
token = None
with open(GITHUB_TOKEN_FILE, 'r') as f:
    token = f.readline().strip()

# get urls with github search
gs = GithubSearch(token)
urls = gs.search_repos(GITHUB_SEARCH_REPO_QUERY, GITHUB_SEARCH_REPO_SORT,
 GITHUB_SEARCH_REPO_ORDER, GITHUB_SEARCH_REPO_LANGUAGE, GITHUB_SEARCH_HAS_FORK,
 GITHUB_SEARCH_REPO_MAXRESULT)

# create json file
JsonMaker.list_to_json(GITHUB_SEARCH_REPO_GENFILE, urls)
