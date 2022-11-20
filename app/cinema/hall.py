from app.people.cinema_staff import Cleaner


class CinemaHall:
    def __init__(self, number: int) -> None:
        self.number = number

    def movie_session(self, movie_name: str, customers: list,
                      cleaning_staff: Cleaner) -> None:

        print(f'"{movie_name}" started in hall number {self.number}.')
        [cust.watch_movie(movie_name) for cust in customers]
        print(f'"{movie_name}" ended.')
        cleaning_staff.clean_hall(self.number)
