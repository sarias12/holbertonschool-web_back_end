#!/usr/bin/env python3
"""
Duck typing - first element of a sequence
"""
from typing import Any, Sequence, List, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """[summary]

    Args:
        lst (Sequence[Any])

    Returns:
        Union[Any, None]
    """
    if lst:
        return lst[0]
    else:
        return None
