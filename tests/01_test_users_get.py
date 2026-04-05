import pytest


class TestGetUsers:

    def test_get_all_users_status_code(self, user_service):
        response = user_service.get_users()
        assert response.status_code == 200

    def test_get_all_users_returns_list(self, user_service):
        response = user_service.get_users()
        data = response.json()
        assert isinstance(data, list)

    def test_get_all_users_not_empty(self, user_service):
        response = user_service.get_users()
        data = response.json()
        assert len(data) > 0

    def test_get_active_users_only(self, user_service):
        response = user_service.get_users_by_status("active")
        data = response.json()
        assert response.status_code == 200
        assert all(user["status"] == "active" for user in data)

    def test_get_single_user_status_code(self, user_service):
        users = user_service.get_users().json()
        user_id = users[0]["id"]
        response = user_service.get_user(user_id)
        assert response.status_code == 200

    def test_get_single_user_has_correct_fields(self, user_service):
        users = user_service.get_users().json()
        user_id = users[0]["id"]
        response = user_service.get_user(user_id)
        data = response.json()
        assert "id" in data
        assert "name" in data
        assert "email" in data
        assert "status" in data
