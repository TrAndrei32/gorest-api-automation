import pytest
import random


class TestDeleteUsers:

    def test_delete_user_status_code_body(self, user_service):
        payload = {
            "name": "Delete me",
            "email": f"deleteme{random.randint(1000, 9999)}@example.com",
            "gender": "male",
            "status": "active"
        }
        created = user_service.create_user(payload).json()
        user_id = created["id"]

        response = user_service.delete_user(user_id)
        assert response.status_code == 204
        assert response.text == ""

    def test_delete_user_no_longer_exists(self, user_service):
        payload = {
            "name": "Temporary User",
            "email": f"temp{random.randint(1000, 9999)}@example.com",
            "gender": "male",
            "status": "active"
        }
        created = user_service.create_user(payload).json()
        user_id = created["id"]

        user_service.delete_user(user_id)
        response = user_service.get_user(user_id)
        assert response.status_code == 404
