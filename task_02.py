#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Warmup tasks for the 14th week"""


from data import FRUIT


def get_cost_per_item(shoplist):
    """gets value of each items

    Args:
        shoplist(dictionary): list of things we buy and their costs
    Returns:
        dictionary with items and their costs

    Examples:
        >>> get_cost_per_item({'Lime': 12, 'Red Pear': 4,
                'Peach': 24, 'Beet': 1})
        {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
    """
    return {key: shoplist[key] * FRUIT[key] for key in shoplist.iterkeys()
            if key in FRUIT}


def get_total_cost(shoplist):
    """returns net cost in a single line of all the things

    Args:
        shoplist(dictionary): list of things we buy and their costs
    Returns:
        net cost of what we buy

    Examples:
        >>>get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
        112.80000000000001
    """
    return sum(val for val in get_cost_per_item(shoplist).itervalues())
