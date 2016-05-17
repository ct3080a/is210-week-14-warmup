#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 Module"""

import pet


class Dog(pet.Pet):
    """Imported Dog subclass from pet.

        Attributes:
        None
    """
    def __init__(self, has_shots=False, **kwargs):
        """Creates a constructor for the Dog class.

            Args:
            has_shots (bool): whether the Dog has shots, default of False
            **kwargs: an arbitrary arguments dictionary

            Returns:
            None
        """
        pet.Pet.__init__(self, **kwargs)
        self.has_shots = has_shots
