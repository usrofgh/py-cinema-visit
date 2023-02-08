from app.cinema.bar import CinemaBar
from app.cinema.hall import CinemaHall

from app.people.cinema_staff import Cleaner
from app.people.customer import Customer


def cinema_visit(
        customers: [dict],
        hall_number: int,
        cleaning_staff: str,
        movie_name: str,
) -> None:
    customers = [Customer(**cust) for cust in customers]
    cleaner = Cleaner(cleaning_staff)

    cinema_hall = CinemaHall(hall_number)
    cinema_bar = CinemaBar()

    for cust in customers:
        cinema_bar.sell_product(cust.food, cust)

    cinema_hall.movie_session(movie_name, customers, cleaner)
