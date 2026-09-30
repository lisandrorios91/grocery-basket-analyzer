# Return the number of units charged (BOGOF halves the quantity).

def item_charged_units(item, bogof_items=None):
    if not item or len(item) < 4:
        return 0
    name, quantity, price, category = item 
    quantity = max(0, quantity)

# Round up if BOGOF charges for only half.
    
    if bogof_items and name in bogof_items:
        charged_units = (quantity + 1) // 2
    else:
        charged_units = quantity
    return charged_units

# Compute the total for a single item after BOGOF and category discounts.

def item_subtotal(item, bogof_items=None, category_discounts=None):
    if not item or len(item) <4:
        return 0.0
    name, quantity, unit_price, category = item

# Handle invalid or negative data.
    
    unit_price = max(0.0, unit_price)

# Apply BOGOF.
    
    charged_units = item_charged_units(item, bogof_items)
    subtotal = charged_units * unit_price

# Apply category discount.
    
    if category_discounts and category in category_discounts:
        discount_rate = category_discounts[category]
        subtotal *= (1 - discount_rate)
    return round(subtotal, 2)

# Return the subtotal of the basket after discounts.
    
def basket_subtotal(basket, bogof_items=None, category_discounts=None):
        if not basket:
            return 0.0
        total = sum(item_subtotal(item, bogof_items, category_discounts) for item in basket)
        return round(total, 2)