#!/usr/bin/env python3
"""Complex types - list of floats
"""

from typing import List


def sum_list(input_list: List[float]) -> float:

    """Function which takes a list of floats and returns theri sum.

    Args:
        input_list (List[float]): List of float numbers

    Returns:
        float: sum of floats
    """
    sum: float = 0.0
    for num in input_list:
        sum += num

    return sum
