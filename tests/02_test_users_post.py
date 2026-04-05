import pytest
import random


class TestPostUsers:

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
