#!/usr/bin/env python3
"""
Let's duck type an iterable object
"""
from typing import List, Sequence, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """[summary]

    Args:
        lst (Iterable)

    Returns:
        List[Tuple[Sequence, int]]
    """
    return [(i, len(i)) for i in lst]
