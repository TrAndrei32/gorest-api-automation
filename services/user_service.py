import requests
from settings import BASE_URL, HEADERS


class UserService:

    def get_users(self):
        return requests.get(f"{BASE_URL}/users", headers=HEADERS)

    def get_users_by_status(self, status):
        return requests.get(f"{BASE_URL}/users?status={status}", headers=HEADERS)

    def get_user(self, user_id):
        return requests.get(f"{BASE_URL}/users/{user_id}", headers=HEADERS)

    def create_user(self, payload):
        return requests.post(f"{BASE_URL}/users", json=payload, headers=HEADERS)

    def update_user(self, user_id, payload):
        return requests.put(f"{BASE_URL}/users/{user_id}", json=payload, headers=HEADERS)

    def delete_user(self, user_id):
        return requests.delete(f"{BASE_URL}/users/{user_id}", headers=HEADERS)
