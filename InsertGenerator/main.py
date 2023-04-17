from course_work import *
from generators import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--destination", type=str, help="Destination file")
parser.add_argument("--db", type=str, help="Database name")
args = parser.parse_args()

DESTINATION_FILE = args.destination
DATABASE_NAME = args.db

if None in [DESTINATION_FILE, DATABASE_NAME]:
    print("Error: Some parameters were not specified!", file=sys.stderr)
    exit()

fill(DESTINATION_FILE, DATABASE_NAME)










