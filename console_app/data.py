from datetime import datetime
from array import array
inventory_transaction_history_array = array("i", [1000, -200, 500, -300, 400])
inventory_transaction_history = [
    (1000.0, datetime(2024, 6, 1, 10, 0)),
    (-200.0, datetime(2024, 6, 2, 14, 30)),
    (500.0, datetime(2024, 6, 3, 9, 15)),
    (-300.0, datetime(2024, 6, 4, 16, 45)),
    (400.0, datetime(2024, 6, 5, 11, 20))
]
user_operation_log = []
supplier_credentials = ("SUP101", "SUP202")
warehouse_locations = {"Warehouse_A", "Warehouse_B"}

product_details = {
    "name": "Cricket Bat ss",
    "category": "Sports",
    "sku": "CBX-SS-2026",
    "current_stock": 100,
    "unit_price": 5000.0
}

REORDER_LEVEL = 25
MINIMUM_STOCK_LEVEL = 50

