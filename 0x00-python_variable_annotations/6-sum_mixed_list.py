#!/usr/bin/env python3
"""
Complex types - Mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function which takes a list  of integers and floats and returns
    their sum

    Args:
        mxd_lst (Union[int, float]): list of integers and floats

    Returns:
        sum of all numbers.
    """
    sum: float = 0.0
    for num in mxd_lst:
        sum += num
    return sum
