"""Some useful adapters"""
from typing import Any

import cipheycore


def id_lambda(value: Any):
    """
        A function used in dynamic class generation that abstracts away a constant return value (like in getName)
    """
    return lambda *args: value


def cached_freq_analysis(ctext, config):
    base = config.objs.setdefault("cached_freq_analysis", ctext)
    res = base.get("cached_freq_analysis")
    if res is not None:
        return res

    base["cached_freq_analysis"] = cipheycore.analyse_string(ctext)
