#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Shopping list."""

from data import FRUIT


def get_cost_per_item(shoplist):
    """Function to get the cost per item in list.

    Args:
        shoplist (int): Key of shoplist found in FRUIT.

    Returns:
         dict: New dictionary keyed by name of fruit with cost per item.

    Examples:
        >>>get_cost_per_item({'Lime': 12, 'Red Pear': 4,
            'Peach': 24, 'Beet': 1})
        {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
    """
    return{item:FRUIT[item] * shoplist[item] for item in shoplist.iterkeys()
        if item in FRUIT}


def get_total_cost(shoplist):
    """Function to calculate total cost of list.

    Args:
        shoplist (str): Name of item as found in FRUIT.

    Returns:
        float: Total cost.

    Examples:
        >>>get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
        112.80000000000001
    """
    return sum(itemtotal for itemtotal in
               get_cost_per_item(shoplist).itervalues())
