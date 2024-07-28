#!/usr/bin/env python3
"""utilities.
"""
import requests
from functools import wraps
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


__all__ = [
    "access_nested_map",
    "get_json",
    "memoize",
]


def access_nested_map(nested_map: Mapping, path: Sequence) -> Any:
    """access_nested_map.
    Para
    ----------
    nested_map: Mapping
    path: Sequence
    """
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]

    return nested_map


def get_json(url: str) -> Dict:
    """get_json.
    """
    response = requests.get(url)
    return response.json()


def memoize(fn: Callable) -> Callable:
    """memoize.
    """
    attr_name = "_{}".format(fn.__name__)

    @wraps(fn)
    def memoized(self):
        """"memoized"""
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return property(memoized)
