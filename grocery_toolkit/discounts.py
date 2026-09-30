from grocery_toolkit.calculations import basket_subtotal

# Apply discount if subtotal exceeds threshold.

def apply_threshold_discount(subtotal, threshold_amount, discount_rate):
    if subtotal < 0:
        subtotal = 0
    if subtotal >= threshold_amount:
        subtotal *= (1 - discount_rate)
    return round(subtotal, 2)

# Compute tax amount.

def compute_tax(subtotal, tax_rate):
    if subtotal <0:
        subtotal = 0
    tax = subtotal * tax_rate
    return round(tax, 2)

# Compute the grand total after all discounts and tax.

def grand_total(basket, *, bogof_items=None, category_discounts=None,
                threshold_amount=0.0, threshold_rate=0.0, tax_rate=0.13):
    subtotal = basket_subtotal(basket, bogof_items, category_discounts)
    discount_subtotal = apply_threshold_discount(subtotal, threshold_amount, threshold_rate)
    tax = compute_tax(discount_subtotal, tax_rate)
    total = discount_subtotal + tax
    return round(total, 2)