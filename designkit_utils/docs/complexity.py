
from typing import Callable, Any, Final as Const
from dataclasses import dataclass
from enum import StrEnum
import inspect



class BigO(StrEnum):
    CONSTANT = 'O(1)'
    AMORTIZED_CONSTANT = 'amortized O(1)'
    LOGARITHMIC = 'O(log n)'
    LINEAR = 'O(n)'
    QUASILINEAR  = 'O(n log n)'
    QUADRATIC = 'O(n^2)'
    EXPONENTIAL = 'O(2^n)'
    CUBIC = 'O(n^3)'
    POLYNOMIAL = 'O(n^k)'
    FACTORIAL = 'O(n!)'

@dataclass(frozen=True)
class Complexity:
    time: BigO
    space: BigO



def complexity(time: BigO, space: BigO) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        func.__complexity__ = Complexity(time, space)
        return func
    return decorator



DEFAULT_FORMAT: Const[dict[str, str]] = {
    'class': '{class}',
    'method': '{method}',
    'time': '{time}',
    'space': '{space}',
}

def collect_complexities(module: Any, format: dict[str, str] | None = None) -> list[dict[str, str]]:
    format = format or DEFAULT_FORMAT

    complexities: list[dict[str, str]] = []

    for _, obj in inspect.getmembers(module):
        if inspect.isclass(obj):

            for name, method in inspect.getmembers(obj):
                complexity: Complexity | None = getattr(method, '__complexity__', None)

                if complexity:
                    entry = {}

                    context = {
                        'class': obj.__name__,
                        'method': name,
                        'time': complexity.time.value,
                        'space': complexity.space.value,
                    }

                    for field, template in format.items():
                        entry[field] = template.format(**context)

                    complexities.append(entry)

    return complexities
