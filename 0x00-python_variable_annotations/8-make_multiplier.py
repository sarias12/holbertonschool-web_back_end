#!/usr/bin/env python3
"""
Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that takes a float multiplier as argument and returns
    a function that multiplies a float by multiplier.

    Args:
        multiplier (float)

    Returns:
        Callable[[float], float]
    """
    def f(num: float) -> float:
        return num * multiplier
    return f
