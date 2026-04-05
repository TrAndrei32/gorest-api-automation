import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://gorest.co.in/public/v2"
TOKEN = os.getenv("GOREST_TOKEN")
HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}
