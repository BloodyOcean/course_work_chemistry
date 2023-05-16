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
        "paths": ["s3://pharmacy-objects/Manufacturers/v1/"],
        "recurse": True,
    },
    transformation_ctx="S3bucket_node1",
)

# Clean up records
def clean_records(rec):
    # Clean up name, description, city, contact person, email (remove all whitespaces at the beginning and the end)
    rec["name"] = rec["name"].strip()
    rec["description"] = rec["description"].strip()
    rec["contact_person"] = rec["contact_person"].strip()
    rec["email"] = rec["email"].strip()

    return rec

cleared_recordes_node = Map.apply(frame=S3bucket_node1, f=clean_records, transformation_ctx="cleared_recordes_node")

# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=cleared_recordes_node,
    mappings=[
        ("name", "string", "name", "string"),
        ("description", "string", "description", "string"),
        ("contact_person", "string", "contact_person", "string"),
        ("email", "string", "email", "string"),
        ("create_date", "string", "create_date", "date"),
    ],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node MySQL table
MySQLtable_node3 = glueContext.write_dynamic_frame.from_catalog(
    frame=ApplyMapping_node2,
    database="pharmacy-glue-db",
    table_name="pharmacy_shop_manufacturers",
    transformation_ctx="MySQLtable_node3",
)

job.commit()
