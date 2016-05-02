#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Groceries"""

from data import FRUIT

def get_cost_per_item(shoplist):
    """Function that returns value of each item

    Arguments:
        shoplist(dict): Shoping Dictionary(Items, Fruits and Costs)

    Return:
        A Dictionary filled with fruits and Costs

    Examples:
        >>> get_cost_per_item({'Beet': 6, 'Red Pear': 5, 'Lime':2, 'Peach': 12})
        {'Peach': 95.76, 'Lime': 7.08}
    """
    return {key: shoplist[key] * FRUIT[key]
            for key in shoplist.iterkeys() if key in FRUIT} #3.5 replaces iterkey
                                                           # with key

def get_total_cost(shoplist):
    """Function that returns total costs of items.

    Arguments:
        shoplist(dict): Shopping list dictionary.

    Return:
        Returns total cost of dictionary.

    Examples:
        >>> get_total_cost({'Lime': 2, 'Apple': 4, 'Peach':6})
        25.12
    """
    return sum(val for val in get_cost_per_item(shoplist).itervalues())
