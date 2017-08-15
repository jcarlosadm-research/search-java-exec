from git import Repo
import urllib.request
import urllib.error

try:
	url = "https://github.com/pacampbell/Game.git"
	req = urllib.request.Request(url)
	urllib.request.urlopen(req)
	Repo.clone_from(url, "./temp")
except urllib.error.HTTPError:
	print("url error")
