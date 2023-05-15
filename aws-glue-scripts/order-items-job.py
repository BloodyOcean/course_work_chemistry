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
        "paths": ["s3://pharmacy-objects/OrderItems/v1/"],
        "recurse": True,
    },
    transformation_ctx="S3bucket_node1",
)

# Convert DynamicFrame to DataFrame
df = S3bucket_node1.toDF()

# Drop duplicates based on order_id and product_id
df_unique = df.dropDuplicates(['order_id', 'product_id'])

# Convert back to DynamicFrame
S3bucket_node1_unique = glueContext.create_dynamic_frame.from_rdd(df_unique.rdd, schema=df_unique.schema, name="S3bucket_node1_unique",)


# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=S3bucket_node1_unique,
    mappings=[
        ("order_id", "int", "order_id", "int"),
        ("product_id", "int", "product_id", "int"),
        ("quantity", "int", "quantity", "int"),
    ],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node MySQL table
MySQLtable_node3 = glueContext.write_dynamic_frame.from_catalog(
    frame=ApplyMapping_node2,
    database="pharmacy-glue-db",
    table_name="pharmacy_shop_order_items",
    transformation_ctx="MySQLtable_node3",
)

job.commit()
