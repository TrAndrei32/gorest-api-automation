import random
import pytest
from jsonschema import validate, ValidationError

USER_SCHEMA = {
    "type": "object",
    "required": ["id", "name", "email", "gender", "status"],
    "properties": {
        "id":     {"type": "integer"},
        "name":   {"type": "string"},
        "email":  {"type": "string"},
        "gender": {"type": "string", "enum": ["male", "female"]},
        "status": {"type": "string", "enum": ["active", "inactive"]}
    },
    "additionalProperties": False
}


class TestSchemaValidation:
    def test_create_user_schema(self, user_service):
        payload = {
            "name": "Schema User",
            "email": f"schema{random.randint(1000, 9999)}@example.com",
            "gender": "male",
            "status": "active"
        }
        response = user_service.create_user(payload)
        data = response.json()
        assert response.status_code == 201
        validate(instance=data, schema=USER_SCHEMA)

    def test_get_user_schema(self, user_service):
        payload = {
            "name": "Get Schema User",
            "email": f"getschema{random.randint(1000, 9999)}@example.com",
            "gender": "female",
            "status": "active"
        }
        created = user_service.create_user(payload).json()
        user_id = created["id"]

        response = user_service.get_user(user_id)
        data = response.json()

        assert response.status_code == 200
        validate(instance=data, schema=USER_SCHEMA)

    def test_schema_invalid_gender(self):
        fake_response = {
            "id": 1,
            "name": "Test",
            "email": "test@example.com",
            "gender": "unknown",
            "status": "active"
        }
        with pytest.raises(ValidationError):
            validate(instance=fake_response, schema=USER_SCHEMA)
