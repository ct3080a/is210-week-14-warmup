#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Warmup task 1 for week 14 exercises"""

from pet import Pet


class Dog(Pet):
    """ The Dog subclass of Pet

    Attributes:
        none.
    """
    def __init__(self, has_shots=False, **kwargs):
        """Constructor for the Dog subclass

        Args:
            has_shots (bool): specifies if the Dog has had its shots yet.

            kwargs (dict): arbitrary keyword arguments list

        Attributes:
            has_shots (bool): specifies if the Dog has had its shots yet.

            see Pet.
        """
        super(Dog, self).__init__(**kwargs)
        self.has_shots = has_shots
