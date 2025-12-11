from cinema import AdvancedStatistics
from logger_config import setup_logging

setup_logging()

cinema = AdvancedStatistics()

while True:
    try:
        print("\n1 - Фильм қосу")
        print("2 - Қарапайым талдау")
        print("3 - Кеңейтілген талдау")
        print("4 - Фильмдер тізімі")
        print("5 - Шығу")
        choice = input("Таңдау: ")

        if choice == "1":
            title = input("Фильм аты: ")
            genre = input("Жанры: ")
            views = int(input("Қаралым саны: "))
            rating = float(input("Рейтинг: "))
            cinema.add_movie(title, genre, views, rating)

        elif choice == "2":
            cinema.analyze()
            cinema.show_report()

        elif choice == "3":
            cinema.analyze_by_categories()
            cinema.show_report()

        elif choice == "4":
            for m in cinema.movies:
                print(m)

        elif choice == "5":
            break
        
        else:
            print("Қате таңдау!")

    except Exception as e:
        print(f"Қате: {e}")
