"""See who's currently in space; get their name and spacecraft"""

from space_request import space_people, spacecraft_name, headers
from organize_space_data import sorted_full_names_space_people, tabulate_table


def people_in_space():
    """
    Retrieve information about people in space: name and spacecraft name.
    Print a tabulated table with this information.
    """

    sorted_full_names = sorted_full_names_space_people()

    table = tabulate_table(sorted_full_names, spacecraft_name, headers)
    print(table)


if __name__ == "__main__":
    people_in_space()
