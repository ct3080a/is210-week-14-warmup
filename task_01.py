#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Warmup tasks for the 14th week"""


import pet


class Dog(pet.Pet):
    """parent class is in pet module

    Attributes:
        None
    """
    def __init__(self, has_shots=False, **kwargs):
        """dog class constructor

        Args:
            has_shots(boolean): defaults to False
        Returns:
            None
         """
        pet.Pet.__init__(self, **kwargs)
        self.has_shots = has_shots
