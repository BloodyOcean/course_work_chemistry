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
        "paths": ["s3://pharmacy-objects/Comments/v1/"],
        "recurse": True,
    },
    transformation_ctx="S3bucket_node1",
)

# Clean up records
def clean_records(rec):

    # Clean up name, description (remove all whitespaces at the beginning and the end)
    rec["comment_text"] = rec["comment_text"].strip()

    return rec

cleared_recordes_node = Map.apply(frame=S3bucket_node1, f=clean_records, transformation_ctx="cleared_recordes_node")

# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=cleared_recordes_node,
    mappings=[
        ("product_id", "int", "product_id", "int"),
        ("customer_id", "int", "customer_id", "int"),
        ("comment_text", "string", "comment_text", "string"),
        ("rating", "int", "rating", "smallint"),
        ("create_date", "string", "create_date", "date"),
    ],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node MySQL table
MySQLtable_node3 = glueContext.write_dynamic_frame.from_catalog(
    frame=ApplyMapping_node2,
    database="pharmacy-glue-db",
    table_name="pharmacy_shop_comments",
    transformation_ctx="MySQLtable_node3",
)

job.commit()
