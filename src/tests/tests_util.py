from search.java.exec import GitUtil
import unittest
import os
import shutil

TEMP_REPOS = os.path.join("tests","temp_repos_test")

class GitUtilTest(unittest.TestCase):
	def test_folder_name(self):
		git_util = GitUtil("https://www.google.com/search/esteros.html")
		self.assertEqual(git_util.foldername,"esteros")
		git_util = GitUtil("https://www.google.com/search/esteros")
		self.assertEqual(git_util.foldername,"esteros")
		git_util = GitUtil("esteros.html")
		self.assertEqual(git_util.foldername,"esteros")
		git_util = GitUtil("esteros")
		self.assertEqual(git_util.foldername,"esteros")
	
	def test_clone(self):
		git_util = GitUtil("https://github.com/pacampbell/Game.git")
		
		self.assertTrue(git_util.clone(TEMP_REPOS))
		self.assertTrue(os.path.exists(os.path.join(TEMP_REPOS,git_util.foldername)))
		
		self.assertTrue(git_util.delete_local_repo())
		self.assertFalse(os.path.exists(os.path.join(TEMP_REPOS,git_util.foldername)))
		
		try:
			shutil.rmtree(TEMP_REPOS)
		except:
			pass
