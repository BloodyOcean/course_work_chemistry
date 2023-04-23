from insert_models import *
from sqlalchemy import create_engine, MetaData, Table, select
from config import CONFIG
from functools import reduce

def main():
    levus_is_so_hot_right_now('customers', 'customers', [map_customers])
    levus_is_so_hot_right_now('product_categories', 'product_categories', [map_product_categorys])
    levus_is_so_hot_right_now('manufacturers', 'manufacturers', [map_manufacturers])
    levus_is_so_hot_right_now('products', 'products', [map_products])
    levus_is_so_hot_right_now('orders', 'orders', [map_orders])
    levus_is_so_hot_right_now('order_items', 'order_items', [map_order_items])
    levus_is_so_hot_right_now('comments', 'comments', [map_comments])
    levus_is_so_hot_right_now('payments', 'payments', [map_payments])

# TODO: rename to 'move_data' after it's not funny anymore
def levus_is_so_hot_right_now(srcTableName, destTableName, data_processors):
    '''
        Moves data from srcTableName to destTableName after getting it through all the processors

        Args:
            data_processors (array): an array of functions. Each of them receives the result of the previous one
        and can do whatever you want. It could be useful if the data should be cleaned before insert.
        For example, you can have a processor to delete some rows, another one to transform some columns,
        and so on.
    '''
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

# TODO: add a parameter for src connection instead of retrieving mariadb connection string from CONFIG
def connect_table(tableName, connection_string):
    '''
        Connects to the mariadb and creates instances of connection and creates a table based on read metadate
        and 'tableName' parameter

        Returns: tuple(connection, table)
    '''
    # create db engine and connect
    db_engine = create_engine(connection_string)
    connection = db_engine.connect()
    # reflect the SQL Server database schema into the MetaData object
    metadata = MetaData()
    metadata.reflect(bind=db_engine)
    
    table = Table(tableName, metadata, autoload=True, autoload_with=db_engine)
    return (connection, table)
    

if __name__ == "__main__":
    main()
