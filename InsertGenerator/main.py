import argparse

from deformation import DiscountDeformation, ShippingDeformation
from lib.config_helper import ConfigHelper
from lib.models_generator import *
from models.models import DbHelper


def main():

    session = get_db_session()

    deformatorDiscount = DiscountDeformation(0.5)
    deformatorShipping = ShippingDeformation(0.5)

    mod_gen = ModelsGenerator(session)
    res = mod_gen.generate_discount(100, deformatorDiscount)
    mod_gen.load_by_lst(res)
    res = mod_gen.generate_shipping(100, deformatorShipping)
    mod_gen.load_by_lst(res)


def get_db_session():
    # Don't use config.example.ini. Just copy it, rename to config.ini and replace example values 
    # with actual ones. In this way stuff that are used in reality won't be revealed on github.
    cfg_helper = ConfigHelper(path='configs/config.example.ini')
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    db_helper = DbHelper(cfg_helper.get('db', 'connection_string'))
    db_helper.connect()
    db_helper.create_tables()
    
    return db_helper.session


if __name__ == '__main__':
    main()
