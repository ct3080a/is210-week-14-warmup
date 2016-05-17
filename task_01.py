#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The module uses arbitrary arguments."""


import pet


class Dog(pet.Pet):
    """ This class is a subclass of Pet."""
    def __init__(self, has_shots=False, **kwargs):
        self.has_shots = has_shots
        pet.Pet.__init__(self, **kwargs)
