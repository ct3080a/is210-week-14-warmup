#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Warmup task 2 for week 14"""

from data import FRUIT


def get_cost_per_item(shoplist):
    """ Calcualates the total cost for each item in the given shopping list

    Args:
        shoplist (dict): list of fruit items to be purchased with the quantity.

    Returns:
        dict: The shoping list of fruits with the total cost for each item for
                the value.

    Examples:
        >>> slist = {'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1}
        >>> get_cost_per_item(slist)
        {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
    """
    return {frt: cnt * FRUIT[frt] for (frt, cnt) in shoplist.iteritems()
            if frt in FRUIT}


def get_total_cost(shoplist):
    """ Calcualates the total for the given shopping list

    Args:
        shoplist (dict): list of fruit items to be purchased with the quantity.

    Returns:
        float: The total of the costs for all of the items in the shopping list.

    Examples:
        >>> slist = {'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1}
        >>> get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
        112.80000000000001
    """
    return sum(get_cost_per_item(shoplist).values())
