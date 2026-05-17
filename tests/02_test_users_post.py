import pytest
import random


class TestPostUsers:

    @pytest.mark.smoke
    def test_create_user_status_code(self, user_service):
        payload = {
            "name": "Test User",
            "email": f"testuser{random.randint(1000, 9999)}@example.com",
            "gender": "male",
            "status": "active"
        }
        response = user_service.create_user(payload)
        assert response.status_code == 201

    def test_create_user_returns_correct_data(self, user_service):
        payload = {
            "name": "John Doe",
            "email": f"johndoe{random.randint(1000, 9999)}@example.com",
            "gender": "male",
            "status": "active"
        }
        response = user_service.create_user(payload)
        data = response.json()
        assert data["name"] == "John Doe"
        assert data["gender"] == "male"
        assert data["status"] == "active"

    def test_create_user_has_id(self, user_service):
        payload = {
            "name": "Jane Doe",
            "email": f"janedoe{random.randint(1000, 9999)}@example.com",
            "gender": "female",
            "status": "active"
        }
        response = user_service.create_user(payload)
        data = response.json()
        assert "id" in data
        assert data["id"] is not None

    def test_create_user_missing_name(self, user_service):
        payload = {
            "email": f"noname{random.randint(1000, 9999)}@example.com",
            "gender": "male",
            "status": "active"
        }
        response = user_service.create_user(payload)
        assert response.status_code == 422


class TestUserStatus:
    def test_create_user_with_status_active(self, user_service):
        payload = {
            "name": "Test Active",
            "email": f"active{random.randint(1000, 9999)}@example.com",
            "gender": "male",
            "status": "active"
        }
        response = user_service.create_user(payload)
        data = response.json()
        assert response.status_code == 201
        assert data["status"] == "active"

    def test_create_user_with_status_inactive(self, user_service):
        payload = {
            "name": "Test Inactive",
            "email": f"inactive{random.randint(1000, 9999)}@example.com",
            "gender": "male",
            "status": "inactive"
        }
        response = user_service.create_user(payload)
        data = response.json()
        assert response.status_code == 201
        assert data["status"] == "inactive"

    def test_create_user_missing_status(self, user_service):
        payload = {
            "name": "No Status User",
            "email": f"nostatus{random.randint(1000, 9999)}@example.com",
            "gender": "male"
        }
        response = user_service.create_user(payload)
        data = response.json()
        assert response.status_code == 422
        assert any(
            error["field"] == "status" for error in data), f"Expected status field error, got: {data}"
