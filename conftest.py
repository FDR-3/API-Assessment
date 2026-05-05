import pytest
import os
from api_clients.tmdb_client import TMDBClient
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def api_key():
  #Pulls key from .env file
  key = os.getenv("TMDB_API_KEY")

  if not key or key.strip() == "" or key == "insert_key_here":
    pytest.fail("TMDB_API_KEY not found in environment variables")

  return key

@pytest.fixture(scope="session")
def tmdb_client(api_key):
  return TMDBClient(api_key=api_key)