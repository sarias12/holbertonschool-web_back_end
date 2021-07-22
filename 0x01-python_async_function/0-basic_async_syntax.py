#!/usr/bin/env python3
"""The basics of async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """[summary]

    Args:
        max_delay (int, optional): last number of de range. Defaults to 10.

    Returns:
        float: delay
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
