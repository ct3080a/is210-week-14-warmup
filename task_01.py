#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Arbitrary Arguments."""

import pet


class Dog(pet.Pet):
    """Imported Pet subclass."""

    def __init__(self, has_shots=False, **kwargs):
        """Constructor class of dog subclassed from Pet.

        Args:
            has_shots (bool): True or False if dog has shots. Default is false.
            arbitrary kwargs: Arbitrary arguments dictionary from pet.Pet

        """
        self.has_shots = has_shots
        pet.Pet.__init__(self, **kwargs)
