from collections import Counter, defaultdict

def get_unique_categories(items: list[dict]) -> set[str]:
    """Повертає множину унікальних категорій (set comprehension)."""
    return {item["category"] for item in items}

def build_product_index(items: list[dict]) -> dict[str, dict]:
    """Створює словниковий індекс для пошуку товару за назвою за O(1) (dict comprehension)."""
    return {item["name"]: item for item in items}

def group_products_by_category(items: list[dict]) -> dict[str, list[dict]]:
    """Групує товари за категоріями з використанням defaultdict."""
    grouped = defaultdict(list)
    for item in items:
        grouped[item["category"]].append(item)
    return dict(grouped)

def count_products_by_category(items: list[dict]) -> Counter:
    """Рахує кількість найменувань у кожній товарній категорії через Counter."""
    return Counter(item["category"] for item in items)