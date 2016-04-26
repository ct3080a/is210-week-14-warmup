#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module uses comprehension tools """

from data import FRUIT


def get_cost_per_item(shoplist):
    """This function has a dictionary argument.
        Argument:
            shoplist mixed: Dictionary

        Returns:
            A dictionary (mixed)
        Examples:
        >>> get_cost_per_item(D)
        {
        'Red Plum': 14.950000000000001,
        'Organic Black Plum': 104.7,
        'Grenade Pluot': 5.97,
        'Peach': 59.85,
        'Forelle Pear': 8.97,
        'Organic Peach': 19.96,
        'Organic Bosc Pear': 13.93,
        'Organic Bartlett Pears': 54.24,
        'White Peach': 47.88,
        'Bosc Pear': 7.96,
        'Anjou Pears': 33.83,
        'Red Pear': 27.39,
        'Organic Anjou Pears': 41.88,
        'Comice Pear': 22.410000000000004,
        'Black Plum': 29.900000000000002,
        'Bartlett Pears': 9.95
        }
    """
    newdict = {
        key: shoplist[key] * FRUIT[key] 
        for key, value in shoplist.iteritems() if key in FRUIT}
    return newdict
D = {
    'Black Plum': 10,
    'Red Plum': 5,
    'Grenade Pluot': 3,
    'Organic Black Plum': 30,
    'Peach': 15,
    'White Peach': 12,
    'Organic Peach': 4,
    'Anjou Pears': 17,
    'Organic Anjou Pears': 12,
    'Bartlett Pears': 5,
    'Organic Bartlett Pears': 16,
    'Bosc Pear': 4,
    'Organic Bosc Pear': 7,
    'Comice Pear': 9,
    'Forelle Pear': 3,
    'Red Pear': 11,
    "aaaa": 55,
    }


def get_total_cost(shoplist):
    """This function returns total cost.
        Argument:
            shoplist mixed: Dictionary
        Returns:
            A float:
        Examples
        >>> get_total_cost(D)
        503.7699999999999
    """
    return sum(get_cost_per_item(shoplist).values())
