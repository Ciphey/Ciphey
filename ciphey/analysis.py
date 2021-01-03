from typing import Union

def freq_analysis(data: Union[str, bytes]):
    tab = {}
    for i in data:
        if tab.get(i):
            tab[i] += 1
        else:
            tab[i] = 0
    return tab

def windowed_freq_analysis(data: Union[str, bytes], window_size: int, skip_space: bool = True):
    check_space = lambda x: False
    if skip_space:
        if type(data) == str:
            check_space = str.isspace
        elif type(data) == bytes:
            check_space = lambda x: x.decode().isspace()
    window = 0
    windows = [{} for i in range(0, window_size)]
    for i in data:
        if not check_space(data):
            continue
        tab = windows[window]
        if tab.get(i):
            tab[i] += 1
        else:
            tab[i] = 0
        window += 1
        window %= window_size
    return windows