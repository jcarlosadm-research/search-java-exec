from search.java.exec.util import GitUtil
from search.java.exec.util import JsonInputFile
from search.java.exec.util import JsonProcessedUrls
from search.java.exec.util import FolderManager
import unittest
import os
import shutil

TEMP_REPOS = os.path.join("tests","temp_repos_test")
TEMP_REPOS2 = os.path.join("tests","temp_repos_test2")

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
        self.assertEqual(git_util.path,os.path.join(TEMP_REPOS,git_util.foldername))
        self.assertTrue(os.path.exists(os.path.join(TEMP_REPOS,git_util.foldername)))
        
        self.assertTrue(git_util.delete_local_repo())
        self.assertFalse(os.path.exists(os.path.join(TEMP_REPOS,git_util.foldername)))
        
        try:
            shutil.rmtree(TEMP_REPOS)
        except:
            pass

class JsonInputFileTest(unittest.TestCase):
    def test_load_jsonfile(self):
        urllist = self.load_list()

        for url in urllist:
            self.assertTrue(url == "https://github.com/thm-projects/arsnova-backend.git" or \
                url == "https://github.com/asciidoctor/asciidoctor-maven-plugin.git")

    def test_size_list(self):
        urllist = self.load_list()

        self.assertEqual(len(urllist), 2)

    def test_duplicates(self):
        urllist = self.load_list()

        second_list = []
        for url in urllist:
            self.assertTrue(url not in second_list)
            second_list.append(url)

    def load_list(self):
        path = os.path.join("tests","resources","repositories_test.json")
        json_file = JsonInputFile(path)
        urllist = json_file.get_urls()

        return urllist

class JsonProcessedUrlsTest(unittest.TestCase):
    def test_add_check(self):
        url1 = "http://google.com"
        url2 = "http://yahoo.com"
        path = os.path.join("tests","json_processed_urls.json")
        
        jsonp_urls = JsonProcessedUrls(path)
        jsonp_urls.add_url(url1)
        jsonp_urls.add_url(url2)
        
        self.assertTrue(jsonp_urls.check_url(url1))
        self.assertTrue(jsonp_urls.check_url(url2))
        
        os.remove(path)

class FolderManagerTest(unittest.TestCase):
    def test_create_and_delete(self):
        path = os.path.join("tests","foldertest")

        self.assertFalse(os.path.exists(path))

        FolderManager.create_folder(path)
        self.assertTrue(os.path.exists(path))

        FolderManager.delete_folder_recursive(path)
        self.assertFalse(os.path.exists(path))

    def test_list_javafiles(self):
        filelist = FolderManager.list_of_javafiles(os.path.join("tests","resources",\
            "repo_test_list"))

        self.assertTrue(os.path.join("tests","resources","repo_test_list","file2.java") \
            in filelist)
        self.assertTrue(os.path.join("tests","resources","repo_test_list","file1.java") \
            in filelist)
        self.assertTrue(os.path.join("tests","resources","repo_test_list","folder02", \
             "file03.java") in filelist)
        self.assertTrue(os.path.join("tests","resources","repo_test_list","folder01", \
            "folder03","folder04","file05.java") in filelist)
        self.assertTrue(len(filelist) == 4)
