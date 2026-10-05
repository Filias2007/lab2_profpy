"""Store Analyzer package.

Модуль обробки структурованих даних, групування, фільтрації 
та аналітики інтернет-магазину.
"""

from store_analyzer.analytics import (
    calculate_aggregate_metrics,
    calculate_total_inventory_value,
    create_product_record,
    create_stock_threshold_filter,
    filter_by_category,
    find_most_expensive_product,
    sort_products_by_price,
)
from store_analyzer.data import STORE_METADATA, products
from store_analyzer.decorators import measure_time
from store_analyzer.processors import (
    build_product_index,
    count_products_by_category,
    get_unique_categories,
    group_products_by_category,
)

__all__ = [
    "STORE_METADATA",
    "products",
    "measure_time",
    "get_unique_categories",
    "build_product_index",
    "group_products_by_category",
    "count_products_by_category",
    "calculate_total_inventory_value",
    "find_most_expensive_product",
    "sort_products_by_price",
    "filter_by_category",
    "create_stock_threshold_filter",
    "calculate_aggregate_metrics",
    "create_product_record",
]