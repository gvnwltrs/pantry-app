#!/usr/bin/env python3 

import pytest

from sections.pantry import Pantry

def test_init():
    pass

def test_pantry_exists():
    pantry = Pantry()
    assert isinstance(pantry, Pantry)
