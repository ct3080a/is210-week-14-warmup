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
 ## enter D and call function with D
        
    """
    newdict = {key: shoplist[key] * FRUIT[key] for key, value in shoplist.iteritems() if key in FRUIT}
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
    'Organic Anjou Pears':12,
    'Bartlett Pears': 5,
    'Organic Bartlett Pears': 16,
    'Bosc Pear': 4,
    'Organic Bosc Pear': 7,
    'Comice Pear': 9,
    'Forelle Pear': 3,
    'Red Pear': 11,
    "aaaa":55,
    }



        



