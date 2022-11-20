from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(customers: list, hall_number: int,
                 cleaning_staff: str, movie_name: str) -> None:

    clients = [Customer(**cust) for cust in customers]
    cleaner = Cleaner(cleaning_staff)

    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()

    [cinema_bar.sell_product(cust.food, cust) for cust in clients]
    cinema_hall.movie_session(movie_name, clients, cleaner)
