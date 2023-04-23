
def map_customers(rows):
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


def map_product_categorys(rows):
    return [{
        'id': str(row[0]),
        'name': row[1],
        'create_date': str(row[2]),
        'update_date': str(row[3])
    } for row in rows]


def map_manufacturers(rows):
    return [{
        'id': str(row[0]),
        'name': row[1],
        'description': row[2],
        'contact_person': row[3],
        'email': row[4],
        'create_date': str(row[5]),
        'update_date': str(row[6])
    } for row in rows]


def map_products(rows):
    return [{
        'id': str(row[0]),
        'name': row[1],
        'description': row[2],
        'price': str(row[3]),
        'quantity': str(row[4]),
        'manufacturer_id': str(row[5]),
        'category_id': str(row[6]),
        'create_date': str(row[7]),
        'update_date': str(row[8])
    } for row in rows]


def map_orders(rows):
    return [{
        'id': str(row[0]),
        'customer_id': str(row[1]),
        'order_date': str(row[2]),
        'status': row[3],
        'create_date': str(row[4]),
        'update_date': str(row[5])
    } for row in rows]


def map_order_items(rows):
    return [{
        'order_id': str(row[0]),
        'product_id': str(row[1]),
        'quantity': str(row[2])
    } for row in rows]


def map_comments(rows):
    return [{
        'id': str(row[0]),
        'product_id': str(row[1]),
        'customer_id': str(row[2]),
        'comment_text': row[3],
        'rating': str(row[4]),
        'create_date': str(row[5]),
        'update_date': str(row[6])
    } for row in rows]


def map_payments(rows):
    return [{
        'id': str(row[0]),
        'order_id': str(row[1]),
        'payment_date': str(row[2]),
        'payment_method': row[3],
        'payment_amount': str(row[4]),
        'card_number': row[5],
        'card_holder': row[6],
        'card_exp_month': str(row[7]),
        'card_exp_year': str(row[8]),
        'card_cvv': row[9]
    } for row in rows]
