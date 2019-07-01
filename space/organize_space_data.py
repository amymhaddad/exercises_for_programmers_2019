"""Organize the data from the API request. Sort each name in alphabetical order by last name"""

from tabulate import tabulate
from space_request import space_people


def sorted_full_names_space_people():
    """Return a sorted list of space people"""
    return sorted(space_people, key=lambda last_name: last_name[-1])


def tabulate_table(sorted_full_names, spacecraft_name, headers):
    """Return a tabulated table with space people's names and spacecraft name"""
    table = [sorted_full_names, spacecraft_name]
    return tabulate(table, headers)
