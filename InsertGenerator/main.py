import argparse

from lib.config_helper import ConfigHelper
from lib.models_generator import ModelsGenerator
from models.models import DbHelper


def main():
    cfg_helper = ConfigHelper()
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    db_helper = DbHelper(cfg_helper.get('db', 'connection_string'))
    db_helper.connect()
    db_helper.create_tables()
    session = db_helper.session
    mod_gen = ModelsGenerator(session)
    res = mod_gen.generate_comment(10)
    mod_gen.load_by_lst(res)


if __name__ == '__main__':
    main()
