#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Task 2 docstring."""


from data import FRUIT


def get_cost_per_item(shoplist):
    """Function that returns a new dictionary keyed by the name of the fruit
       with the total cost per-item reflected.

       Args:
           shoplist(dict): keys and values found in FRUIT

        Return:
            {key: shoplist[key] * FRUIT[key]: dictionary of the fruit with total
                                              cost per-item

        Examples:

        >>> get_cost_per_item({'Lime': 12, 'Red Pear': 4, 'Peach': 24,
        'Beet': 1})
        {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
    """
    return {key: shoplist[key] * FRUIT[key]
            for key in shoplist.iterkeys() if key in FRUIT}


def get_total_cost(shoplist):
    """Function that returns the total cost.

        Args:
            shoplist(dict): keys and values found in FRUIT

        Return:
            value: Total cost

        Examples:

            >>>get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24,
            'Beet': 1})
            112.80000000000001
    """
    return sum(value for value in get_cost_per_item(shoplist).itervalues())
