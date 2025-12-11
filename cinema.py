import logging
import yaml
from base import MovieAnalyzer
from analyzer import MovieTextAnalyzer

log = logging.getLogger(_name_)

with open("config.yaml", "r", encoding="utf-8") as f:
    CONFIG = yaml.safe_load(f)["app"]

class CinemaStatistics(MovieAnalyzer):
    def _init_(self):
        self._movies = []
        self._results = {}

    @property
    def movies(self):
        return self._movies

    def add_movie(self, title, genre, views, rating):
        try:
            MovieTextAnalyzer.lexical_check(title)
            MovieTextAnalyzer.syntax_check(genre)

            if not CONFIG["allow_negative_views"] and views < 0:
                raise ValueError("Қаралым саны теріс болмауы керек")

            if rating > CONFIG["max_rating"]:
                raise ValueError("Рейтинг шектен жоғары")

            film = {
                "title": title,
                "genre": genre,
                "views": views,
                "rating": rating
            }

            log.info(f"Фильм қосылды: {film}")
            self._movies.append(film)

        except Exception as e:
            log.error(f"Фильмді қосу қатесі: {e}")
            raise

    def analyze(self):
        if not self._movies:
            log.warning("Талдау үшін фильм жоқ")
            return

        total_views = sum(m['views'] for m in self._movies)
        avg_rating = sum(m['rating'] for m in self._movies) / len(self._movies)
        most_popular = max(self._movies, key=lambda x: x['views'])

        genres = {}
        for m in self._movies:
            genres[m['genre']] = genres.get(m['genre'], 0) + m['views']

        self._results = {
            "total_views": total_views,
            "avg_rating": round(avg_rating, 2),
            "most_popular": most_popular,
            "genres": genres
        }

        log.info("Қарапайым талдау орындалды")

    def show_report(self):
        if not self._results:
            print("Алдымен analyze() орындаңыз!")
            return

        print("\n--- ҚАРАПАЙЫМ ТАЛДАУ ---")
        print(f"Жалпы қаралым саны: {self._results['total_views']}")
        print(f"Орташа рейтинг: {self._results['avg_rating']}")
        print(f"Ең танымал фильм: {self._results['most_popular']['title']}")

#Расширенный класс

class AdvancedStatistics(CinemaStatistics):
    def _init_(self):
        super()._init_()
        self._user_categories = {}

    def analyze_by_categories(self):
        super().analyze()

        genre_ratings = {}
        for m in self._movies:
            genre_ratings.setdefault(m['genre'], []).append(m['rating'])

        for genre, ratings in genre_ratings.items():
            avg_rating = sum(ratings) / len(ratings)
            self._user_categories[genre] = {
                "avg_rating": round(avg_rating, 2),
                "movies_count": len(ratings)
            }

        log.info("Кеңейтілген талдау орындалды")

    def show_report(self):
        super().show_report()

        if self._user_categories:
            print("\n--- ЖАНРЛАР БОЙЫНША ТОЛЫҚ ТАЛДАУ ---")
            for g, info in self._user_categories.items():
                print(f"{g}: орташа рейтинг {info['avg_rating']}, фильм саны {info['movies_count']}")
