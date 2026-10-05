import random
from time import perf_counter
from store_analyzer.data import STORE_METADATA, products
from store_analyzer.processors import (
    build_product_index,
    count_products_by_category,
    get_unique_categories,
    group_products_by_category,
)
from store_analyzer.analytics import (
    calculate_aggregate_metrics,
    calculate_total_inventory_value,
    create_product_record,
    create_stock_threshold_filter,
    filter_by_category,
    find_most_expensive_product,
    sort_products_by_price,
)

def print_table(title: str, items: list[dict]) -> None:
    print(f"\n{title}")
    print("-" * 75)
    print(f"{'Назва':<25}{'Категорія':<16}{'Ціна (грн)':>12}{'К-сть':>8}{'Разом (грн)':>14}")
    print("-" * 75)
    for p in items:
        total = p["price"] * p["quantity"]
        print(f"{p['name']:<25}{p['category']:<16}{p['price']:>12.2f}{p['quantity']:>8}{total:>14.2f}")

def run_benchmark() -> None:
    print("\n" + "=" * 65)
    print("ЕКСПЕРИМЕНТАЛЬНИЙ БЕНЧМАРК: List Search vs Dict Search")
    print("=" * 65)
    sizes = [1_000, 10_000, 100_000]
    
    for size in sizes:
        synthetic_data = [
            {"id": i, "name": f"Item_{i}", "category": "Tech", "price": 100.0, "quantity": 1}
            for i in range(size)
        ]
        target_name = f"Item_{size - 1}"
        dict_index = {item["name"]: item for item in synthetic_data}
        
        # Лінійний пошук у list
        start = perf_counter()
        _ = next((item for item in synthetic_data if item["name"] == target_name), None)
        list_time = perf_counter() - start
        
        # Пошук за ключем у dict
        start = perf_counter()
        _ = dict_index.get(target_name)
        dict_time = perf_counter() - start
        
        print(f"Записів: {size:<7} | List O(n): {list_time:.8f} с | Dict O(1): {dict_time:.8f} с | Прискорення: {list_time / max(dict_time, 1e-12):.1f}x")

def main() -> None:
    print(f"=== Ініціалізація аналізу складу: {STORE_METADATA[0]} ({STORE_METADATA[1]}) ===")
    print_table("Базовий каталог товарів", products)
    
    categories = get_unique_categories(products)
    print(f"\nУнікальні категорії товару (set): {categories}")
    
    total_val = calculate_total_inventory_value(products)
    print(f"\nЗагальна вартість залишків на складі: {total_val:,.2f} грн")
    
    most_expensive = find_most_expensive_product(products)
    if most_expensive:
        print(f"Найдорожчий товар: {most_expensive['name']} за ціною {most_expensive['price']:.2f} грн")
        
    print_table("Сортування за спаданням ціни", sort_products_by_price(products))
    
    counts = count_products_by_category(products)
    print("\nКількість найменувань товарів у категоріях (Counter):")
    for cat, cnt in counts.items():
        print(f"  * {cat}: {cnt} поз.")
        
    grouped = group_products_by_category(products)
    print(f"\nГрупування товарів (defaultdict): сформовано груп — {len(grouped)}")
    
    index = build_product_index(products)
    query = "Механічна клавіатура"
    found = index.get(query)
    print(f"\nШвидкий пошук через dict-index за назвою '{query}':")
    print(f"  Результат: {found}")
    
    # Використання Closure
    low_stock_limit = 5
    is_critical_stock = create_stock_threshold_filter(low_stock_limit)
    critical_items = [p for p in products if is_critical_stock(p)]
    print_table(f"Товари з критичним залишком (< {low_stock_limit} од.) [Closure filter]", critical_items)
    
    # Використання *args та **kwargs
    sample_metrics = calculate_aggregate_metrics(28500.0, 750.0, 9200.0, 3100.0)
    print(f"\nСтатистика цін через *args: {sample_metrics}")
    
    new_product = create_product_record(name="Навушники Pro", category="Аксесуари", price=4200.0, quantity=15)
    print(f"\nСтворено новий товар через **kwargs: {new_product}")
    
    run_benchmark()

if __name__ == "__main__":
    main()