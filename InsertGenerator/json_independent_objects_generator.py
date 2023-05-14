import json
import os

import deformation as deformation
from lib.models_generator import *

from main import get_db_session

# Function to create a directory if it doesn't exist and paste all objects from the list to this directory
def paste_to_dir(object_list, dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

    for i in range(1, len(object_list) + 1):
        file_name = f"{i}.json"
        file_path = os.path.join(dir, file_name)

        # Serialize the objects to the JSON file
        with open(file_path, "w") as f:
            json.dump(object_list[i - 1].to_json(), f)

                
def generate_and_upload_independent_objects(gen_version): 
    session = get_db_session()

    customers_deformator = deformation.CustomerDeformation(0.5)
    shipping_deformator = deformation.ShippingDeformation(0.5)
    discount_deformator = deformation.DiscountDeformation(0.5)
    produt_category_deformator = deformation.CategoryDeformation(0.5)
    manufacturer_deformator = deformation.ManufacturerDeformation(0.5)
    supplier_deformator = deformation.SupplierDeformation(0.5)
    packaging_deformator = deformation.PackagingDeformation(0.5)


    mod_gen = ModelsGenerator(session)

    # Generate objects
    customers = mod_gen.generate_customers(250, customers_deformator)
    shippings = mod_gen.generate_shipping(250, shipping_deformator)
    discounts = mod_gen.generate_discount(40, discount_deformator)
    product_categories = mod_gen.generate_categories(35, produt_category_deformator)
    manufacturers = mod_gen.generate_manufacturer(75, manufacturer_deformator)
    suppliers = mod_gen.generate_supplier(115, supplier_deformator)
    packagings = mod_gen.generate_packaging(33, packaging_deformator)


    # Define objects' directories
    directory_customers = f"./InsertGenerator/GeneratedJson/Customers/{gen_version}"
    directory_shippings = f"./InsertGenerator/GeneratedJson/Shippings/{gen_version}"
    directory_discounts = f"./InsertGenerator/GeneratedJson/Discounts/{gen_version}"
    directory_product_categories = f"./InsertGenerator/GeneratedJson/ProductCategories/{gen_version}"
    directory_manufacturers = f"./InsertGenerator/GeneratedJson/Manufacturers/{gen_version}"
    directory_suppliers = f"./InsertGenerator/GeneratedJson/Suppliers/{gen_version}"
    directory_packagings = f"./InsertGenerator/GeneratedJson/Packagings/{gen_version}"

    # Paste objects to directories 
    paste_to_dir(customers, directory_customers)
    paste_to_dir(shippings, directory_shippings)
    paste_to_dir(discounts, directory_discounts)
    paste_to_dir(product_categories, directory_product_categories)
    paste_to_dir(manufacturers, directory_manufacturers)
    paste_to_dir(suppliers, directory_suppliers)
    paste_to_dir(packagings, directory_packagings)

generate_and_upload_independent_objects("v1")