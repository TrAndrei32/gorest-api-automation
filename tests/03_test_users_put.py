import pytest
import random


class TestPutUsers:
    def test_update_user_status_code(self, user_service):
        payload = {
            "name": "Update User",
            "email": f"updated{random.randint(1000, 9999)}@example.com",
            "gender": "male",
            "status": "active"
        }
        created = user_service.create_user(payload).json()
        user_id = created["id"]

        update_payload = {"name": "New Name"}
        response = user_service.update_user(user_id, update_payload)
        assert response.status_code == 200

    def test_update_user_name_changes(self, user_service):
        payload = {
            "name": "Original Name",
            "email": f"original{random.randint(1000, 9999)}@example.com",
            "gender": "female",
            "status": "active"
        }
        created = user_service.create_user(payload).json()
        user_id = created["id"]

        update_payload = {"name": "Changed Name"}
        response = user_service.update_user(user_id, update_payload)
        data = response.json()
        assert data["name"] == "Changed Name"

    def test_update_user_status_changes(self, user_service):
        payload = {
            "name": "Status User",
            "email": f"status{random.randint(1000, 9999)}@example.com",
            "gender": "male",
            "status": "active"
        }
        created = user_service.create_user(payload).json()
        user_id = created["id"]

        update_payload = {"status": "inactive"}
        response = user_service.update_user(user_id, update_payload)
        data = response.json()
        assert data["status"] == "inactive"

    def test_update_nonexistent_user(self, user_service):
        response = user_service.update_user(999999999, {"name": "Ghost"})
        assert response.status_code == 404
