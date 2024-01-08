MAX_SUM = 25


def sum_digits(num: str):
    return sum(int(n) for n in num)


def sum_coordinates(coordinates: tuple[int, int]):
    return sum_digits(''.join(str(i) for i in coordinates))


def right(coordinates: tuple[int, int]):
    return coordinates[0] + 1, coordinates[1]


def up(coordinates: tuple[int, int]):
    return coordinates[0], coordinates[1] + 1


def ant_max_available_coordinates(coordinates: tuple[int, int], coordinates_set: set = None):
    coordinates_set = coordinates_set or set()
    coordinates_set.add(coordinates)
    for move in (right, up):
        if sum_coordinates(new := move(coordinates)) <= MAX_SUM and new not in coordinates_set:
            ant_max_available_coordinates(new, coordinates_set)
    return coordinates_set


if __name__ == '__main__':
    all_coordinates = ant_max_available_coordinates(coordinates=(1000, 1000))
    print(len(all_coordinates))
