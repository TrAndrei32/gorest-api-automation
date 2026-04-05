# Gorest API Automation

API test automation project built with Python, Pytest, and Requests against the [Gorest.co.in](https://gorest.co.in) public API. The project follows a Service Layer pattern, covering full CRUD operations with Bearer token authentication.

---

## Tech Stack

- Python 3.12
- Pytest
- Requests
- python-dotenv
- pytest-html

---

## Project Structure
```
gorest-api-automation/
├── .github/
│   └── workflows/
│       └── ci.yml
├── services/
│   └── user_service.py
├── tests/
│   ├── 01_test_users_get.py
│   ├── 02_test_users_post.py
│   ├── 03_test_users_put.py
│   └── 04_test_users_delete.py
├── .env
├── .gitignore
├── conftest.py
├── requirements.txt
└── settings.py
```
---

## Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/gorest-api-automation.git
cd gorest-api-automation
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure authentication

Create a `.env` file in the root folder:
GOREST_TOKEN=your_token_here
Get your free token at [gorest.co.in](https://gorest.co.in) by logging in with Google or GitHub.

---

## Running Tests

| Command | Description |
|---------|-------------|
| `pytest -v` | Run all tests |
| `pytest tests/01_test_users_get.py -v` | Run a specific suite |
| `pytest -v --html=reports/report.html --self-contained-html` | Run with HTML report |

---

## Test Coverage

| Suite | Tests | Operations |
|-------|-------|------------|
| GET | 6 | Get all users, filter by status, get single user, validate response fields |
| POST | 4 | Create user, validate response data, negative test (missing field) |
| PUT | 4 | Update user name, update user status, negative test (nonexistent user) |
| DELETE | 2 | Delete user and verify response, verify user no longer exists |

**Total: 16 tests**

---

## CI/CD

The project includes a GitHub Actions pipeline configured with `workflow_dispatch` for manual triggering.

> **Note:** Gorest.co.in uses Cloudflare protection which blocks GitHub Actions shared runners (IP addresses from Microsoft Azure datacenters). All 16 tests pass locally. The pipeline can be triggered manually from the Actions tab when needed.

---

## Authentication

The project uses Bearer token authentication. The token is stored locally in a `.env` file which is excluded from version control via `.gitignore`. In CI/CD environments, the token is injected via GitHub Secrets.