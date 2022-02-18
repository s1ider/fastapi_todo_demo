from locust import HttpUser, task, between
from fastapi_todo.app import PREFIX


class SiteUser(HttpUser):
    access_token: str = None

    def on_start(self):
        r = self.client.post(f"{PREFIX}/users/login", 
        {"username":"dz@gmail.com", "password":"secret_pwd"})
        r_json = r.json()
        self.access_token = r_json['access_token']

    def on_stop(self):
        print("logging out")

    @task
    def users_list(self):
        self.client.get(f'{PREFIX}/users')

    @task
    def profile(self):
        user = 'dz@gmail.com'
        self.client.get(f'{PREFIX}/users/{user}')

    @task(2)
    def get_todo(self):
        self.client.get(f'{PREFIX}/todos',)
        # headers={'Authorization': f'Bearer {self.access_token}'})
