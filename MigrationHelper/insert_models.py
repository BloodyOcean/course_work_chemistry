
def map_discounts(rows) -> list[dict]:
    return [{
        'id': str(row[0]),
        'title': row[1],
        'description': row[2],
        'start_date': str(row[3]),
        'end_date': str(row[4]),
        'discount_percent': str(row[5]),
        'create_date': str(row[6]),
        'update_date': str(row[7])
    } for row in rows]


def map_packaging(rows) -> list[dict]:
    return [{
        'id': str(row[0]),
        'name': row[1],
        'description': row[2],
        'create_date': str(row[3]),
        'update_date': str(row[4])
    } for row in rows]


def map_suppliers(rows) -> list[dict]:
    return [{
        'id': str(row[0]),
        'name': row[1],
        'contact_name': row[2],
        'phone_number': row[3],
        'email': row[4],
        'address': row[5],
        'create_date': str(row[6]),
        'update_date': str(row[7])
    } for row in rows]


def map_customers(rows) -> list[dict]:
    return [
        {
            'id': str(row[0]),
            'first_name': row[1],
            'last_name': row[2],
            'email': row[3],
            'phone_number': row[4],
            'address': row[5],
            'city': row[6],
            'state': row[7],
            'zip_code': row[8],
            'create_date': str(row[9]),
            'update_date': str(row[10])
        } for row in rows
    ]


def map_product_categories(rows) -> list[dict]:
    return [{
        'id': str(row[0]),
        'name': row[1],
        'create_date': str(row[2]),
        'update_date': str(row[3])
    } for row in rows]


def map_manufacturers(rows) -> list[dict]:
    return [{
        'id': str(row[0]),
        'name': row[1],
        'description': row[2],
        'contact_person': row[3],
        'email': row[4],
        'create_date': str(row[5]),
        'update_date': str(row[6])
    } for row in rows]


def map_products(rows) -> list[dict]:
    return [{
        'id': str(row[0]),
        'name': row[1],
        'description': row[2],
        'price': str(row[3]),
        'quantity': str(row[4]),
        'manufacturer_id': str(row[5]),
        'supplier_id': str(row[6]),
        'packaging_id': str(row[7]),
        'discount_id': str(row[8]),
        'category_id': str(row[9]),
        'create_date': str(row[10]),
        'update_date': str(row[11])
    } for row in rows]


def map_position(rows) -> list[dict]:
    return [{
        'id': str(row[0]),
        'title': row[1],
        'salary': str(row[2]),
        'create_date': str(row[3]),
        'update_date': str(row[4])
    } for row in rows]


def map_employee(rows) -> list[dict]:
    return [{
        'id': str(row[0]),
        'name': row[1],
        'position_id': str(row[2]),
        'email': row[3],
        'phone_number': row[4],
        'address': row[5],
        'date_of_birth': str(row[6]),
        'hire_date': str(row[7]),
        'create_date': str(row[8]),
        'update_date': str(row[9])
    } for row in rows]


def map_work_schedule(rows) -> list[dict]:
    return [{
        'id': str(row[0]),
        'employee_id': str(row[1]),
        'start_date': str(row[2]),
        'end_date': str(row[3]),
        'start_time': str(row[4]),
        'end_time': str(row[5]),
        'create_date': str(row[6]),
        'update_date': str(row[7])
    } for row in rows]


def map_orders(rows) -> list[dict]:
    return [{
        'id': str(row[0]),
        'employee_id': str(row[1]),
        'shipping_id': str(row[2]),
        'customer_id': str(row[3]),
        'order_date': str(row[4]),
        'status': row[5],
        'create_date': str(row[6]),
        'update_date': str(row[7])
    } for row in rows]


def map_order_items(rows) -> list[dict]:
    return [{
        'order_id': str(row[0]),
        'product_id': str(row[1]),
        'quantity': str(row[2]),
        'create_date': str(row[3]),
        'update_date': str(row[4])
    } for row in rows]


def map_comments(rows) -> list[dict]:
    return [{
        'id': str(row[0]),
        'product_id': str(row[1]),
        'customer_id': str(row[2]),
        'comment_text': row[3],
        'rating': str(row[4]),
        'create_date': str(row[5]),
        'update_date': str(row[6])
    } for row in rows]


def map_payments(rows) -> list[dict]:
    return [{
        'id': str(row[0]),
        'order_id': str(row[1]),
        'payment_date': str(row[2]),
        'payment_method': row[3],
        'payment_amount': str(row[4]),
        'card_number': row[5],
        'card_holder': row[6],
        'create_date': str(row[7]),
        'update_date': str(row[8])
    } for row in rows]


def map_shipping(rows) -> list[dict]:
    return [{
        'id': str(row[0]),
        'delivery_date': str(row[1]),
        'carrier': row[2],
        'receiver': row[3],
        'tracking_number': row[4],
        'shipping_address': row[5],
        'shipping_city': row[6],
        'shipping_state': row[7],
        'shipping_zip': row[8],
        'create_date': str(row[9]),
        'update_date': str(row[10])
    } for row in rows]
