#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for a shopping list."""

from data import FRUIT


def get_cost_per_item(shoplist):
    """A docstring for a function using a dictionary for cost per item.

    Args:
        shoplist(dict): Key and value of fruit items from FRUIT.

    Returns:
        dict: New dictionary keyed by name of fruit with cost per item.

    Examples:

        >>> get_cost_per_item({'Lime': 12, 'Red Pear': 4,
            'Peach': 24, 'Beet': 1})
        {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
        """
    return{item: FRUIT[item] * shoplist[item]
           for item in shoplist.iterkeys() if item in FRUIT}

    def get_total_cost(shoplist):
        """A docstring for a functiion using a dictionary for total cost.

        Args:
            shoplist(list): Key and value of fruit items from FRUIT.

        Returns:
            float: Total cost of fruit items.

        Examples:

            >>> get_total_cost({'Lime': 12, 'Red Pear': 4,
                'Peach': 24, 'Beet': 1})
            112.80000000000001
        """
        return sum(itemtotal for itemtotal in
                   get_cost_per_item(shoplist).itervalues())
