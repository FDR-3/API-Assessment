def test_get_popular_movies_status_code(tmdb_client):
  """
  Test 4: Verify the "movie/popular" endpoint returns a 200 OK.
  Ensures you can get a list of popular movies.
  """
  response = tmdb_client.get_popular_movies()

  assert response.status_code == 200

def test_search_movie_by_title(tmdb_client):
  """
  Test 5: Search for 'Inception' and verify the first result is correct.
  Ensures the search algorithm and database indexing are working.
  """
  response = tmdb_client.search_movies("Inception")
  data = response.json()

  assert data["results"][0]["original_title"] == "Inception"

def test_movie_details_structure(tmdb_client):
  """
  Test 6: Verify the schema of a movie details response.
  Ensures the response data has the expected fields.
  """
  movie_id = 550 #Fight Club
  response = tmdb_client.get_movie_details(movie_id)
  data = response.json()
  expected_keys = ["id", "budget", "genres", "overview", "release_date"]

  for key in expected_keys:
    assert key in data

def test_invalid_movie_id_404(tmdb_client):
  """
  Test 7 (Non-Happy Path): Request a non-existent movie ID.
  Ensures the API handles invalid IDs with a graceful 404 error.
  """
  response = tmdb_client.get_movie_details(99999999)

  assert response.status_code == 404