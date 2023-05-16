import deformation as deformation
from lib.config_helper import ConfigHelper
from lib.models_generator import *
from models.models import DbHelper

from json_independent_objects_generator import paste_to_dir
from main import get_db_session


def generate_and_upload_second_level_objects(gen_version):

    session = get_db_session()

    comments_deformator = deformation.CommentDeformation(0.5)
    payments_deformator = deformation.PaymentDeformation(0.5)
    order_items_deformator = deformation.OrderItemDeformation(0.5)


    mod_gen = ModelsGenerator(session)

    # Generate objects
    comments = mod_gen.generate_comment(60, comments_deformator)
    payments = mod_gen.generate_payments(99, payments_deformator)
    order_items = mod_gen.generate_order_item(55, order_items_deformator)

    # Define objects' directories
    directory_comments = f"./InsertGenerator/GeneratedJson/Comments/{gen_version}"
    directory_payments = f"./InsertGenerator/GeneratedJson/Payments/{gen_version}"
    directory_order_items = f"./InsertGenerator/GeneratedJson/OrderItems/{gen_version}"

    # Paste objects to directories
    paste_to_dir(payments, directory_payments)
    paste_to_dir(comments, directory_comments)
    paste_to_dir(order_items, directory_order_items)

generate_and_upload_second_level_objects("v1")