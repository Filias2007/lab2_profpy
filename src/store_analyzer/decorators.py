from functools import wraps
from time import perf_counter
from typing import Any, Callable

def measure_time(func: Callable) -> Callable:
    """Декоратор для заміру часу виконання аналітичних функцій."""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = perf_counter()
        result = func(*args, **kwargs)
        elapsed = perf_counter() - start_time
        print(f"[BENCHMARK] Функція {func.__name__} виконана за: {elapsed:.8f} с")
        return result
    return wrapper