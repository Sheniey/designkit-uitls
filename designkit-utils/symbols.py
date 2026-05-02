
from typing import Final as Const

from .colors import (
    CYAN,
    GRAY,
    LIME,
    RED,
    YELLOW,
)

SUCCESS: Const[str] = f'[{LIME} bold]' + '\\[✓]' + '[/]'
WARNING: Const[str] = f'[{YELLOW} bold]' + '\\[!]' + '[/]'
ERROR: Const[str] = f'[{RED} bold]' + '\\[✗]' + '[/]'
INFO: Const[str] = f'[{CYAN} bold]' + '\\[i]' + '[/]'
NOTE: Const[str] = f'[{GRAY} bold]' + '\\[#]' + '[/]'
