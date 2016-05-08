#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01."""

import pet


class Dog(pet.Pet):
    """Object subclass from Pet Class."""

    def __init__(self, has_shots=False, **args):
        """Constructor for Dog class.

        Args:
            has_shots (boolean, optional): Defaults to False
            *arg (mixed): Arbitrary arg
        """
        self.has_shots = has_shots
        pet.Pet.__init__(self, **args)
