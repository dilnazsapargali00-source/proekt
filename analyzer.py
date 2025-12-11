import re

class MovieTextAnalyzer:
    """Жай лексикалық және синтаксистік талдау"""

    @staticmethod
    def lexical_check(text: str):
        """Тек әріптер мен сандарға рұқсат"""
        if not re.match(r"^[\w\s\-.,:!?'А-Яа-яӘәӨөҰұҮүҚқҒғІі]+$", text):
            raise ValueError("Мәтінде рұқсат етілмеген символдар бар")
        return True

    @staticmethod
    def syntax_check(genre: str):
        """Жанр бір сөзден немесе екі сөзден тұруы керек"""
        if len(genre.split()) > 2:
            raise ValueError("Жанр атауы өте ұзақ")
        return True
