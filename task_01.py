#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Task 1 docstring."""


import pet


class Dog(pet.Pet):
    """Subclassed from Pet."""

    def __init__(self, has_shots=False, **kwargs):
        """Constructor for the Dog class.

        Args:
            has_shots (boolean): Defaults to False.
            **kwargs (dict):  An arbitrary arguments dictionary.
        """
        self.has_shots = has_shots
        pet.Pet.__init__(self, **kwargs)
