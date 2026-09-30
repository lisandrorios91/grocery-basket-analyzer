from grocery_toolkit.calculations import item_subtotal
from grocery_toolkit.discounts import grand_total

# Return the category and the total after the discounts.

def category_breakdown(basket, *, bogof_items=None, category_discounts=None):
    breakdown = {}
    if not basket:
        return breakdown
    for item in basket:
        _,_,_, category = item
        total = item_subtotal(item, bogof_items, category_discounts)
        breakdown[category] = breakdown.get(category, 0) + total
    return {tx: round(ty, 2) for tx, ty in breakdown.items()}

# Return the name of the basket with the lowest grand total.

def cheapest_basket(baskets, *, bogof_items=None, category_discounts=None,
                    threshold_amount=0.0, threshold_rate=0.0, tax_rate=0.13):
    if not baskets:
        return None
    cheapest_name = None
    cheapest_value = float('inf')
    for name, basket in baskets.items():
        total = grand_total(basket,
                            bogof_items = bogof_items,
                            category_discounts = category_discounts,
                            threshold_amount = threshold_amount,
                            threshold_rate = threshold_rate,
                            tax_rate = tax_rate)
        if total < cheapest_value:
            cheapest_value = total
            cheapest_name = name
    return cheapest_name