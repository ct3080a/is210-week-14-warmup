#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""No Sweat my Pet"""

import pet


class Dog(pet.Pet):
    """A class from imported from the pet module.

    Attribute:
        None
    """
    def __init__(self, has_shots=False, **kwargs):
        """A dog class Constructor.

        Arguments:
            has_shots(bool): Boolean attribute that defaults to False

        Return:
            None.
        """
        pet.Pet.__init__(self, **kwargs)
        self.has_shots = has_shots
