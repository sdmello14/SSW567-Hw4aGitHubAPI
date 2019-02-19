import requests
import json

"""
Method to return the list of repositories and 
number of commits in each repository
for the given git ID
"""
def get_Repo_commits(gitId):
    """Dictionary to hold the repositories name as key and number of commits as value"""
    result = dict()
    """Get request to get list of repositories for given gitId"""
    repo_url = "https://api.github.com/users/"+gitId+"/repos"
    repo_resp = requests.get(repo_url)
    repos = repo_resp.json()
    for repo in repos:
        """Get request to get number of commits of each repository"""
        commit_url = "https://api.github.com/repos/"+gitId+"/"+repo['name']+"/commits"
        resp = requests.get(commit_url)
        commit = resp.json()
        """save the repo name and total commit in dict"""
        result[repo['name']] = len(commit)
    return result

def main():
    gitId = input("Please enter git ID:")
    result = get_Repo_commits(gitId)
    """display the repositories and number of commits"""
    for key,value in result.items():
        print("Repo",key,"Number of commits:",value)

import unittest
"""unitTest to test git hub api"""
class TestGitHubAPI(unittest.TestCase):
    def test_repo_commit(self):
        self.assertEqual(13, len(get_Repo_commits("sdmello14")))
        self.assertEqual(1, get_Repo_commits("sdmello14").get("Homework-ssw810"))
        self.assertEqual(23, get_Repo_commits("sdmello14").get("CS555tmJQSS2018Spring"))
        self.assertIsNone(get_Repo_commits("sdmello14").get("abc"))

if __name__ == '__main__':
        unittest.main(exit=False, verbosity=2)

"""if __name__ == "__main__":
    main()"""