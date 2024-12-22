import os
import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()


class KinoPoiskAPI:
    def __init__(self):
        """
        Инициализирует API ключ и базовый URL из переменных окружения.
        :return: None
        """
        self.api_key = os.getenv("API_KEY")
        self.base_url = os.getenv("BASE_URL")

    def search_movie_by_title(self, title: str) -> requests.Response:
        """
        Метод для поиска фильма по названию.
        :param title: Название фильма для поиска.
        :return: requests.Response - ответ API с результатами поиска.
        """
        url = f"{self.base_url}/v1.2/movie/search?page=1&limit=1&query={title}"
        headers = {"X-API-KEY": self.api_key}
        response = requests.get(url, headers=headers)
        return response

    def search_movies_by_actor_id(self, actor_id: int) -> requests.Response:
        """
        Метод для поиска фильмов по ID актера.
        :param actor_id: ID актера для поиска.
        :return: requests.Response - ответ API с фильмами, в которых участвует
        актер.
        """
        url = f"{self.base_url}/v1.4/movie?persons.id={
            actor_id}&persons.enProfession=actor"
        headers = {"X-API-KEY": self.api_key}
        response = requests.get(url, headers=headers)
        return response

    def search_movies_by_genre_and_year(
            self, genre: str, year_range: str) -> requests.Response:
        """
        Метод для поиска фильмов по жанру и диапазону годов выпуска.
        :param genre: Жанр фильма.
        :param year_range: Диапазон годов (например, "2010-2020").
        :return: requests.Response - ответ API с фильмами, соответствующими
        критериям.
        """
        url = f"{self.base_url}/v1.4/movie?genres.name={
            genre}&year={year_range}"
        headers = {"X-API-KEY": self.api_key}
        response = requests.get(url, headers=headers)
        return response

    def search_movies_by_rating_and_country(
            self, rating: str, country: str) -> requests.Response:
        """
        Метод для поиска фильмов по рейтингу и стране.
        :param rating: Диапазон рейтинга (например, "7-10").
        :param country: Название страны.
        :return: requests.Response - ответ API с фильмами, соответствующими
        критериям.
        """
        url = f"{self.base_url}/v1.4/movie?rating.kp={
            rating}&countries.name={country}"
        headers = {"X-API-KEY": self.api_key}
        response = requests.get(url, headers=headers)
        return response

    def search_movies_by_director_id(
            self, director_id: int) -> requests.Response:
        """
        Метод для поиска фильмов по ID режиссера.
        :param director_id: ID режиссера для поиска.
        :return: requests.Response - ответ API с фильмами, снятыми режиссером.
        """
        url = f"{self.base_url}/v1.4/movie?persons.id={
            director_id}&persons.enProfession=director"
        headers = {"X-API-KEY": self.api_key}
        response = requests.get(url, headers=headers)
        return response
