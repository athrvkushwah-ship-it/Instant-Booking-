Movie = [
    {'movie name': 'Goolmal 1', 'code': 1},
    {'movie name': 'Goolmal 2', 'code': 2},
    {'movie name': 'Goolmal 3', 'code': 3},
    {'movie name': 'Goolmal 4', 'code': 4},
    {'movie name': 'Goolmal 5', 'code': 5},
]


def validate_movie(movie_name):

    for movie in Movie:

        if movie['movie name'] == movie_name:
            return True

    return False


def validate_quantity(quantity):

    if quantity >= 1:
        return True

    return False