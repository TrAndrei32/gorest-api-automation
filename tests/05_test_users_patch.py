import pytest
import random
from services.user_service import UserService


class TestPatchUsers:
    def test_patch_user_name_only(self, user_service):
        payload = {
            "name": "Original Name",
            "email": f"patch{random.randint(1000, 9999)}@example.com",
            "gender": "male",
            "status": "active"
        }
        created = user_service.create_user(payload).json()
        user_id = created["id"]
        response = user_service.patch_user(user_id, {"name": "Patched Name"})
        data = response.json()
        assert response.status_code == 200
        assert data["name"] == "Patched Name"
        assert data["gender"] == "male"
        assert data["status"] == "active"

    def test_patch_user_status_only(self, user_service):
        payload = {
            "name": "Status Test",
            "email": f"patchstatus{random.randint(1000, 9999)}@example.com",
            "gender": "female",
            "status": "active"
        }
        created = user_service.create_user(payload).json()
        user_id = created["id"]
        response = user_service.patch_user(user_id, {"status": "inactive"})
        data = response.json()
        assert response.status_code == 200
        assert data["status"] == "inactive"
        assert data["name"] == "Status Test"
        assert data["gender"] == "female"

    def test_patch_nonexistent_user(self, user_service):
        response = user_service.patch_user(999999999, {"name": "Ghost"})
        assert response.status_code == 404
