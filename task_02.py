#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 2."""

from data import FRUIT


def get_cost_per_item(shoplist):
    """Creates dict keyed by fruit name.

    Args:
        shoplist (dict): Dictionary of items.

    Returns:
        dict: Keyed by fruit name and total cost/item.

    Examples:
        >>> get_cost_per_item({'Lime': 12, 'Red Pear': 4,
        'Peach': 24, 'Beet': 1})
        {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}

        >>> get_cost_per_item({''Red Plum': 3,
        'Bosc Pear': 5, 'Key Lime': 2, 'Beet': 1})

        {'Red Plum': 8.97, 'Key Lime': 7.98, 'Bosc Pear': 9.95}
    """
    return {k: v * z for k, v in shoplist.iteritems()
            for x, z in FRUIT.iteritems() if k == x}


def get_total_cost(shoplist):
    """Returns total costs of shoplist.

    Args:
        shoplist (dict): Dictionary of items.

    Returns:
        int: Total costs.

    Examples:
        >>>get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
        112.8

        >>>get_total_cost({'Red Plum': 3,
        'Bosc Pear': 5, 'Key Lime': 2, 'Beet': 1}
        26.900000000000002
    """
    return sum(get_cost_per_item(shoplist).itervalues())
