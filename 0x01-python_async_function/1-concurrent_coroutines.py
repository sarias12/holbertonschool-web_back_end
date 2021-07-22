#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """[summary]

    Args:
        n (int)
        max_delay (int)

    Returns:
        List[float]
    """
    delays_list: List[float] = []
    sorted_delays: List[float] = []
    for index in range(n):
        delays_list.append(wait_random(max_delay))
    for delay in asyncio.as_completed(delays_list):
        earliest_result = await delay
        sorted_delays.append(earliest_result)
    return sorted_delays
