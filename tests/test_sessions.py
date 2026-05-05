def test_unauthorized_access():
  """
  Test 1 (Security): Attempt a call without an API Key.
  Ensures the API gateway properly enforces authentication.
  """
  from api_clients.tmdb_client import TMDBClient
  bad_client = TMDBClient(api_key="invalid_key")
  response = bad_client.get_popular_movies()

  assert response.status_code == 401

def test_creating_guest_session(tmdb_client):
  """
  Test 2: Creates a guest session with the authentication/guest_session/new end point.
  Ensures guests can create sessions.
  """
  response = tmdb_client.create_guess_session()
  data = response.json()

  assert response.status_code == 200
  assert data["success"] is True
  assert "guest_session_id" in data

def test_deleting_invalid_session_id(tmdb_client):
  """
  Test 3 (Non-Happy Path): Attempt to delete a non-existent session ID.
  Ensures the API properly validates session tokens and returns 401 Unauthorized.
  """
  invalid_session = "this_is_not_a_real_id"
  response = tmdb_client.delete_session(invalid_session)

  assert response.status_code == 404
  data = response.json()
  assert data["success"] is False