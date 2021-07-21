#!/usr/bin/env python3
"""More involved type annotations
"""
from typing import Any, Mapping, Union, TypeVar
T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """[summary]

    Args:
        dct (Mapping)
        key (Any)
        default (Union[T, None], optional):  Defaults to None.

    Returns:
        Union[Any, T]
    """
    if key in dct:
        return dct[key]
    else:
        return default
