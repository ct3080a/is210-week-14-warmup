#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for arbitrary args module."""

import pet


class Dog(pet.Pet):
    """Using Pet subclass from pet."""

    def __init__(self, has_shots=False, **kwargs):
        """A docstring for Dog class constructor.

        Args:
            has_shots(bool): True or false if the dog has shots. Default: False.
            arbitrary kwargs: Arbitrary argument dictionary from pet.Pet class.

        Returns:
            None

        Examples:
            None
        """
        self.has_shots = has_shots
        pet.Pet.__init__(self, **kwargs)
