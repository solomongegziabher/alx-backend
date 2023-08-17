#!/usr/bin/env python3
"""simple helper function"""
import csv
import math
from typing import List, Tuple


def index_range(page, page_size):
    """returns a tuple of size two containing a start index and
    an end index corresponding to the range of indexes to return
    in a list for those particular pagination parameters"""
    last_page = page * page_size
    start = last_page - page_size
    tup = (start, last_page)
    return tup


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """add function docstring"""
        assert type(page) == int and type(page_size) == int \
            and page > 0 and page_size > 0
        try:
            tup_range = index_range(page, page_size)
            first = tup_range[0]
            last = tup_range[1]
            lst = self.dataset()
            paginated = lst[first:last]
        except IndexError:
            return []
        return paginated
