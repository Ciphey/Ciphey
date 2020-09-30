"""Some useful adapters"""
from typing import Any, List
import inspect

import cipheycore


def id_lambda(value: Any):
    """
        A function used in dynamic class generation that abstracts away a constant return value (like in getName)
    """
    return lambda *args: value


def fix_case(target: str, base: str) -> str:
    """Returns the lower-case string target with the case of base"""
    ret = ''.join([target[i].upper() if base[i].isupper() else target[i] for i in range(len(target))])
    return ''.join([target[i].upper() if base[i].isupper() else target[i] for i in range(len(target))])
