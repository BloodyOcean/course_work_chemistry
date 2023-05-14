import deformation as deformation
from lib.models_generator import *

from json_independent_objects_generator import paste_to_dir

from main import get_db_session

def generate_and_upload_first_level_objects(gen_version):

    session = get_db_session()

    products_deformator = deformation.ProductDeformation(0.5)
    orders_deformator = deformation.OrderDeformation(0.5)


    mod_gen = ModelsGenerator(session)

    # Generate objects
    products = mod_gen.generate_products(50, products_deformator)
    orders = mod_gen.generate_orders(100, orders_deformator)

    # Define objects' directories
    directory_products = f"./InsertGenerator/GeneratedJson/Products/{gen_version}"
    directory_orders = f"./InsertGenerator/GeneratedJson/Orders/{gen_version}"

    # Paste objects to directories 
    paste_to_dir(products, directory_products)
    paste_to_dir(orders, directory_orders)

generate_and_upload_first_level_objects("v1")