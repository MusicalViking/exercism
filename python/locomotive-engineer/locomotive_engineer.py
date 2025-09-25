"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons.

    :param: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    wagons_list = []
    for wagon in args:
        wagons_list.append(wagon)
    return wagons_list


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - list of wagons.
    """
    # Remove the first two wagons (they need to be moved to the end)
    first_two = each_wagons_id[:2]
    remaining_wagons = each_wagons_id[2:]

    # Find the locomotive (ID 1) and insert missing wagons after it
    locomotive_index = remaining_wagons.index(1)
    fixed_wagons = (remaining_wagons[:locomotive_index + 1] +
                   missing_wagons +
                   remaining_wagons[locomotive_index + 1:])

    # Add the first two wagons to the end
    return fixed_wagons + first_two


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param: arbitrary number of stops.
    :return: dict - updated route dictionary.
    """
    updated_route = route.copy()
    updated_route["stops"] = list(kwargs.values())
    return updated_route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict -  extra route information.
    :return: dict - extended route information.
    """
    extended_route = route.copy()
    extended_route.update(more_route_information)
    return extended_route


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    if not wagons_rows or not wagons_rows[0]:
        return []

    # Get the number of rows and columns
    num_rows = len(wagons_rows)
    num_cols = len(wagons_rows[0])

    # Create the transposed matrix
    transposed = []
    for col in range(num_cols):
        new_row = []
        for row in range(num_rows):
            new_row.append(wagons_rows[row][col])
        transposed.append(new_row)

    return transposed
