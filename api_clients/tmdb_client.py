import requests

class TMDBClient:
  def __init__(self, api_key, base_url="https://api.themoviedb.org/3"):
    self.api_key = api_key
    self.base_url = base_url

  def _get(self, endpoint, params=None):
    if params is None:
      params = {}

    params["api_key"] = self.api_key
    response = requests.get(f"{self.base_url}/{endpoint}", params=params)

    return response
  
  def _delete(self, endpoint, params=None, json_data=None):
    if params is None:
      params = {}
      
    params["api_key"] = self.api_key
    response = requests.delete(f"{self.base_url}/{endpoint}", params=params, json=json_data)

    return response

  def create_guess_session(self):
    return self._get("authentication/guest_session/new")
  
  def delete_session(self, session_id):
    payload = {"session_id": session_id}
    return self._delete("authentication/session", json_data=payload)
    
  def get_movie_details(self, movie_id):
    return self._get(f"movie/{movie_id}")

  def search_movies(self, query):
    return self._get("search/movie", params={"query": query})
  
  def get_popular_movies(self):
    return self._get("movie/popular")
  
  def get_popular_people(self):
    return self._get("person/popular")
  
  def get_person_details(self, person_id):
    return self._get(f"person/{person_id}")
  
  def search_actors(self, query):
    return self._get("search/person", params={"query": query})