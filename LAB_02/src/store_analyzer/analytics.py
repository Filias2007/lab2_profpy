from collections.abc import Callable
from typing import Any
from store_analyzer.decorators import measure_time

@measure_time
def calculate_total_inventory_value(items: list[dict]) -> float:
    """Обчислює загальну вартість залишків складу з використанням generator expression."""
    return sum(item["price"] * item["quantity"] for item in items)

def find_most_expensive_product(items: list[dict]) -> dict | None:
    """Визначає найдорожчий товар асортименту з використанням lambda."""
    if not items:
        return None
    return max(items, key=lambda item: item["price"])

def sort_products_by_price(items: list[dict], descending: bool = True) -> list[dict]:
    """Сортує асортимент за ціною."""
    return sorted(items, key=lambda item: item["price"], reverse=descending)

def filter_by_category(items: list[dict], category: str) -> list[dict]:
    """Фільтрує товари за категорією за допомогою list comprehension."""
    target = category.strip().lower()
    return [item for item in items if item["category"].lower() == target]

def create_stock_threshold_filter(threshold: int) -> Callable[[dict], bool]:
    """Closure (замикання): повертає предикат для фільтрації товарів із залишком нижче threshold."""
    def predicate(item: dict) -> bool:
        return item["quantity"] < threshold
    return predicate

def calculate_aggregate_metrics(*values: float) -> dict[str, float]:
    """Приклад використання *args для обчислення статистичних параметрів довільного набору чисел."""
    if not values:
        return {"count": 0.0, "sum": 0.0, "average": 0.0}
    total = sum(values)
    return {"count": float(len(values)), "sum": total, "average": total / len(values)}

def create_product_record(**attributes: Any) -> dict[str, Any]:
    """Приклад використання **kwargs для гнучкого динамічного створення запису товару."""
    return dict(attributes)