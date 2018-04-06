from github import Github, GithubException
from time import sleep, time
import datetime
import math
import sys
import os

class GithubSearch:
    def __init__(self, token):
        self.token = token

    # TODO: now, max_results is useless. this search always returns 1000 results or less
    # implement for cases: stars, created_at, updated_at
    def search_repos(self, query, sort, order, language, contains_fork, max_results):
        urls = []

        github_obj = Github(self.token)

        results = github_obj.search_repositories(query, sort=sort,
            order=order, language=language, fork=contains_fork)
        total = results.totalCount
        if total > 1000:
            total = 1000

        count = 0
        while count < total:
            try:
                repository = results[count]
                if not repository.fork:
                    urls.append(repository.clone_url)

                count+=1
            except GithubException as e:
                print("\n################################")
                print("error: " + str(e))

                time_to_reset = github_obj.rate_limiting_resettime - time()
                time_to_reset = math.ceil(time_to_reset)

                print(" waiting " + str(time_to_reset) + " seconds.....")
                print(" time to reset: " + datetime.datetime.fromtimestamp( \
                                github_obj.rate_limiting_resettime).strftime( \
                                '%Y-%m-%d %H:%M:%S'))
                sleep(time_to_reset)
                print("\n################################")

            except KeyboardInterrupt:
                try:
                    sys.exit(0)
                except SystemExit:
                    os._exit(0)
            except:
                count+=1

        return urls
