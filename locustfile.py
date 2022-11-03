import time

from locust import HttpUser, task, between

class WebsiteTest(HttpUser):
    wait_time = between(1, 5)

    @task
    '''
    Get github user information
    '''
    def github_get_user(self):
        url = 'users/KimConcepcion'
        with self.client.get(url) as response:
            print(response.json())

    @task
    '''
    Get github user repos information
    '''
    def github_get_repos(self):
        url = 'users/KimConcepcion/repos'
        with self.client.get(url) as response:
            print(response.json())
