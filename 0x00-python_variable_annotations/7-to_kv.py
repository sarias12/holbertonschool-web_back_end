#!/usr/bin/env python3
"""Complex types - string and int/float to tuple
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple:
    """Function that takes a string and a number and return a tuple

    Args:
        k (str): first element for kv tuple
        v (Union[int, float]): Second element for kv tuple

    Returns:
        Tuple: string and number
    """
    kv: Tuple[str, float] = (k, float(v ** 2))
    return kv
