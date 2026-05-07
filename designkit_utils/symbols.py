
from typing import Final as Const

from .colors import (
    CYAN,
    GRAY,
    LIME,
    RED,
    YELLOW,
)

SUCCESS_SYMBOL: Const[str] = '\\[✓]'
WARNING_SYMBOL: Const[str] = '\\[!]'
ERROR_SYMBOL: Const[str] = '\\[✗]'
INFO_SYMBOL: Const[str] = '\\[i]'
NOTE_SYMBOL: Const[str] = '\\[#]'

SUCCESS: Const[str] = f'[{LIME} bold]' + SUCCESS_SYMBOL + '[/]'
WARNING: Const[str] = f'[{YELLOW} bold]' + WARNING_SYMBOL + '[/]'
ERROR: Const[str] = f'[{RED} bold]' + ERROR_SYMBOL + '[/]'
INFO: Const[str] = f'[{CYAN} bold]' + INFO_SYMBOL + '[/]'
NOTE: Const[str] = f'[{GRAY} bold]' + NOTE_SYMBOL + '[/]'
