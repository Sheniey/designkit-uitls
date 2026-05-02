
from typing import Final as Const

from .colors import (
    CYAN,
    GRAY,
    LIME,
    RED,
    YELLOW,
)

SUCCESS: Const[str] = f'[{LIME}]' + '\\[✓]' + '[/]'
WARNING: Const[str] = f'[{YELLOW}]' + '\\[!]' + '[/]'
ERROR: Const[str] = f'[{RED}]' + '\\[✗]' + '[/]'
INFO: Const[str] = f'[{CYAN}]' + '\\[i]' + '[/]'
NOTE: Const[str] = f'[{GRAY}]' + '\\[#]' + '[/]'
