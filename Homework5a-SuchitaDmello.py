import Homework4a_SuchitaDmello
import unittest
from unittest import mock


"""unitTest to test git hub api using mock"""
class TestGitHubAPI(unittest.TestCase):
    @mock.patch('requests.get')
    def test_repo_commit(self,mockedReq):
        mockedReq.return_value.json.return_value = ([{"id":123,"name":"repo1"},{"id":"xyz","name":"repo2"}])
        """test total repository"""
        self.assertEqual(2, len(Homework4a_SuchitaDmello.get_Repo_commits("sdmello14")))

        """test the number of commit in repository"""
        self.assertEqual(2, Homework4a_SuchitaDmello.get_Repo_commits("sdmello14").get("repo1"))
        self.assertEqual(2, Homework4a_SuchitaDmello.get_Repo_commits("sdmello14").get("repo2"))

if __name__ == '__main__':
        unittest.main(exit=False, verbosity=2)
