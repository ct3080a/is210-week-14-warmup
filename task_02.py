#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 Module"""

from data import FRUIT


def get_cost_per_item(shoplist):
    """Defines a function to get the cost of items in the shop list.

        Args:
            shoplist (dict): Dictionary with a key of the item name from FRUIT,
            and a value for the number of units.

        Returns:
            dict: New dictionary keyed by the name of the fruit with the total
            cost per item.

        Example:
            >>> print shoplist
            {'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1}
            >>> get_cost_per_item({'Lime': 12, 'Red Pear': 4, 'Peach': 24,
            'Beet': 1})
            {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
    """
    return{key: FRUIT[key] * shoplist[key]
           for key in shoplist.iterkeys() if item in FRUIT}


def get_total_cost(shoplist):
    """Defines a function to calculate the cost of a list.

        Args:
            shoplist (dict): Dictionary with a key of the item name from FRUIT,
            and a value for the number of units.

        Returns:
            int: total cost of the items in the list.

        Examples:
            >>> get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24,
            'Beet': 1})
            112.80000000000001
    """
    return sum(val for val in get_cost_per_item(shoplist).itervalues())
