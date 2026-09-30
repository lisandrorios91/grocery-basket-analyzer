# Grocery Basket Analyzer

A modular Python package that prices grocery baskets using real retail pricing rules: buy-one-get-one-free offers, category discounts, spend-threshold discounts and sales tax. It also reports spending by category and finds the cheapest basket.

**Tools:** Python 3 (standard library only) · modular package design

## What it does

Each item is a tuple `(name, quantity, unit_price, category)`, and a basket is a list of items. The toolkit applies pricing in the same order a checkout would:

```
item quantity ──► BOGOF (pay for half) ──► category discount ──► item subtotal
                                                                      │
basket subtotal ◄─────────────────────── sum of all items ◄───────────┘
      │
      ├──► threshold discount (e.g. 10% off orders ≥ $20)
      └──► + sales tax (e.g. 13% HST) ──► grand total
```

## Package structure

```
grocery-basket-analyzer/
├── main.py                  # demo script that runs every function
└── grocery_toolkit/
    ├── __init__.py          # exposes all functions at package level
    ├── calculations.py      # item and basket level pricing
    ├── discounts.py         # threshold discount, tax, full pricing pipeline
    └── analysis.py          # category breakdown, cheapest basket comparison
```

| Module | Functions |
|---|---|
| `calculations.py` | `item_charged_units`, `item_subtotal`, `basket_subtotal` |
| `discounts.py` | `apply_threshold_discount`, `compute_tax`, `grand_total` |
| `analysis.py` | `category_breakdown`, `cheapest_basket` |

## Design decisions

- **Reuse over repetition.** Higher-level functions build on the lower ones: `grand_total` calls `basket_subtotal`, which calls `item_subtotal`. Each pricing rule lives in exactly one place.
- **Keyword-only arguments** (`*`) on the pipeline and analysis functions, so discount and tax settings can't be passed in the wrong order by mistake.
- **Defensive inputs.** Negative quantities and prices are treated as 0, and empty baskets or missing discount settings return safe defaults instead of crashing.
- **Money is rounded to 2 decimals** at every step.

## Example output

```
$ python main.py

3. Testing basket_subtotal:
   BasketA subtotal: 27.31
   BasketB subtotal: 23.47
   BasketC subtotal: 35.35

6. Testing grand_total:
   BasketA grand total: 27.78
   BasketB grand total: 23.87
   BasketC grand total: 35.96

7. Testing category_breakdown:
   BasketA category breakdown: {'produce': 2.11, 'dairy': 3.49, 'dry': 3.78, 'bakery': 2.65, 'meat': 15.28}

8. Testing cheapest_basket:
   Cheapest basket: BasketB
```

## How to run

```bash
python main.py
```

No external libraries are needed.

## Context

Individual assignment for a Python programming course in the Master of Data Analytics at the University of Niagara Falls Canada (2025). The `main.py` demo script was provided by the course. The `grocery_toolkit` package is my own work.
