from insert_models import *
from sqlalchemy import create_engine, MetaData, Table, select, Connection
from config import CONFIG
from functools import reduce


def main():
    move_data('suppliers', 'suppliers', [map_suppliers])
    move_data('packaging', 'packaging', [map_packaging])
    move_data('discounts', 'discounts', [map_discounts])
    move_data('customers', 'customers', [map_customers])
    move_data('product_categories', 'product_categories', [map_product_categories])
    move_data('manufacturers', 'manufacturers', [map_manufacturers])
    move_data('products', 'products', [map_products])
    move_data('shipping', 'shipping', [map_shipping])
    move_data('position', 'position', [map_position])
    move_data('employee', 'employee', [map_employee])
    move_data('work_schedule', 'work_schedule', [map_work_schedule])
    move_data('orders', 'orders', [map_orders])
    move_data('order_items', 'order_items', [map_order_items])
    move_data('comments', 'comments', [map_comments])
    move_data('payments', 'payments', [map_payments])


def move_data(srcTableName: str, destTableName: str, data_processors: list) -> None:
    """
        Moves data from srcTableName to destTableName after getting it through all the processors

        :param data_processors is an array of functions. Each of them receives the result of the previous one
        and can do whatever you want. It could be useful if the data should be cleaned before insert.
        For example, you can have a processor to delete some rows, another one to transform some columns,
        and so on.
    """
    src_conn_string = CONFIG['connectionStrings']['sourceConnection']
    dest_conn_string = CONFIG['connectionStrings']['destinationConnection']

    # open connections and create table instances
    (src_conn, src_table) = connect_table(srcTableName, src_conn_string)
    (dest_conn, dest_table) = connect_table(destTableName, dest_conn_string)
    # select data from the table
    select_sql_server = select(src_table)
    result_proxy = src_conn.execute(select_sql_server)
    data = result_proxy.fetchall()
    # run the data through all the processors
    data_to_insert = reduce(lambda d, proc: proc(d), data_processors, data)
    # insert the data
    dest_conn.execute(dest_table.insert(), data_to_insert)
    dest_conn.commit()
    src_conn.close()
    dest_conn.close()


def connect_table(tableName: str, connection_string: str) -> tuple[Connection, Table]:
    """
        Connects to the mariadb and creates instances of connection and creates a table based on read metadate
        and 'tableName' parameter
    """
    # create db engine and connect
    db_engine = create_engine(connection_string)
    connection = db_engine.connect()
    # reflect the SQL Server database schema into the MetaData object
    metadata = MetaData()
    metadata.reflect(bind=db_engine)

    table = Table(tableName, metadata, autoload=True, autoload_with=db_engine)
    return connection, table


if __name__ == "__main__":
    main()
