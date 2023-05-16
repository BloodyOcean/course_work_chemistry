import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://pharmacy-objects/Payments/v1/"],
        "recurse": True,
    },
    transformation_ctx="S3bucket_node1",
)

# Clean up records
def clean_records(rec):

    # Clean up name, description (remove all whitespaces at the beginning and the end)
    rec["card_holder"] = rec["card_holder"].strip()
    rec["card_number"] = rec["card_number"].strip()
    
    return rec

cleared_recordes_node = Map.apply(frame=S3bucket_node1, f=clean_records, transformation_ctx="cleared_recordes_node")

# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=cleared_recordes_node,
    mappings=[
        ("order_id", "int", "order_id", "int"),
        ("payment_date", "string", "payment_date", "date"),
        ("payment_method", "string", "payment_method", "string"),
        ("payment_amount", "double", "payment_amount", "decimal"),
        ("card_number", "string", "card_number", "string"),
        ("card_holder", "string", "card_holder", "string"),
        ("create_date", "string", "create_date", "date"),
    ],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node MySQL table
MySQLtable_node3 = glueContext.write_dynamic_frame.from_catalog(
    frame=ApplyMapping_node2,
    database="pharmacy-glue-db",
    table_name="pharmacy_shop_payments",
    transformation_ctx="MySQLtable_node3",
)

job.commit()
