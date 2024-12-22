import allure
from API.pages.kinopoisk_api import KinoPoiskAPI


class TestKinoPoiskAPI:
    api = KinoPoiskAPI()

    @allure.step("Поиск фильма по названию.")
    def test_search_movie_by_title(self):
        with allure.step(
            "Ввести название фильма в поисковую строку и нажать кнопку поиск."
         ):
            response = self.api.search_movie_by_title("Холоп")
            assert response.status_code == 200
            assert "Холоп" in response.text

    @allure.step("Поиск фильмов по идентификатору актера.")
    def test_search_movies_by_actor_id(self):
        with allure.step("Ввести ID актера и выполнить поиск фильмов."):
            response = self.api.search_movies_by_actor_id(1189311)
            assert response.status_code == 200
            assert len(response.json().get("docs", [])) > 0

    @allure.step("Поиск фильмов по жанру и году.")
    def test_search_movies_by_genre_and_year(self):
        with allure.step("Ввести жанр и диапазон годов для поиска фильмов."):
            response = self.api.search_movies_by_genre_and_year(
                "драма", "2010-2020")
            assert response.status_code == 200
            assert len(response.json().get("docs", [])) > 0

    @allure.step("Поиск фильмов по рейтингу и стране.")
    def test_search_movies_by_rating_and_country(self):
        with allure.step("Ввести рейтинг и страну для поиска фильмов."):
            response = self.api.search_movies_by_rating_and_country(
                "7-10", "США")
            assert response.status_code == 200
            assert len(response.json().get("docs", [])) > 0

    @allure.step("Поиск фильмов по идентификатору режиссера.")
    def test_search_movies_by_director_id(self):
        with allure.step("Ввести ID режиссера и выполнить поиск фильмов."):
            response = self.api.search_movies_by_director_id(1212038)
            assert response.status_code == 200
            assert len(response.json().get("docs", [])) > 0

    # Негативные тесты
    @allure.step("Проверка слишком большого лимита.")
    def test_limit_too_large(self):
        with allure.step("Ввести слишком большой лимит и проверить ответ."):
            response = self.api.search_movies_by_rating_and_country(
                "300", "США")
            assert response.status_code == 400

    @allure.step("Проверка недопустимого значения рейтинга.")
    def test_invalid_rating_value(self):
        with allure.step(
         "Ввести недопустимое значение рейтинга и проверить ответ."):
            response = self.api.search_movies_by_rating_and_country(
                "11-20", "США")
            assert response.status_code == 400

    @allure.step("Проверка недопустимого типа данных.")
    def test_invalid_data_type(self):
        with allure.step(
         "Ввести недопустимое значение типа данных и проверить ответ."):
            response = self.api.search_movies_by_rating_and_country(
                "не_число", "США")
            assert response.status_code == 400

    @allure.step("Проверка недопустимого значения года.")
    def test_invalid_year_value(self):
        with allure.step(
         "Ввести недопустимое значение года и проверить ответ."):
            response = self.api.search_movies_by_genre_and_year(
                "драма", "1850")
            assert response.status_code == 400

    @allure.step("Проверка недопустимого формата типа.")
    def test_invalid_type_format(self):
        with allure.step("Ввести недопустимый формат типа и проверить ответ."):
            response = self.api.search_movies_by_rating_and_country(
                "rating_7.5", "США")
            assert response.status_code == 400

    @allure.step("Проверка недопустимого формата идентификатора.")
    def test_invalid_id_format(self):
        with allure.step(
         "Ввести недопустимый формат идентификатора и проверить ответ."):
            response = self.api.search_movies_by_director_id("id_12345")
            assert response.status_code == 400
