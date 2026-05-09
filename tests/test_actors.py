def test_get_popular_people_status_code(tmdb_client):
  """
  Test 8: Verify the Popular Actors "person/popular" end point returns a 200 OK.
  Ensures you can get a list of popular actors.
  """
  response = tmdb_client.get_popular_people()

  assert response.status_code == 200

def test_get_actor_by_id(tmdb_client):
  """
  Test 9: Get an actors details using the "person/{person_id}" end point.
  Ensures you can get an actor's details by ID.
  """
  person_id = 31 #Tom Hanks
  response = tmdb_client.get_person_details(person_id)
  data = response.json()

  assert data["name"] == "Tom Hanks"

def test_search_actor_by_name(tmdb_client):
  """
  Test 10: Search for "Tom Hanks" and verify the first result is correct.
  Ensures the search algorithm and database indexing are working.
  """
  response = tmdb_client.search_actors("Tom Hanks")
  data = response.json()

  assert data["results"][0]["name"] == "Tom Hanks"