#!/usr/bin/env python3
"""
Definition for index_range helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Args:
        Accepts two integer arguments and generates a
        tuple of size two, which specifies the start and
        end indexes defining the desired range for pagination within a list,
        based on the provided pagination parameters.
        page (int): page number to return (pages are 1-indexed)
        page_size (int): number of items per page
    Return:
        tuple(start_index, end_index)
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size

    return (start, end)
