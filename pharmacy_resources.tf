################################# CONFIGURE REGION ############################################


provider "aws" {
  region = "eu-central-1"
}


################################# CREATE VPC AND SUBNETS ############################################
resource "aws_vpc" "pharmacy_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "pharmacy_vpc"
  }
}


resource "aws_subnet" "pharmacy_subnet_1" {
  vpc_id     = aws_vpc.pharmacy_vpc.id
  cidr_block = "10.0.1.0/24"
  tags = {
    Name = "pharmacy_subnet_1"
  }
}


resource "aws_subnet" "pharmacy_subnet_2" {
  vpc_id     = aws_vpc.pharmacy_vpc.id
  cidr_block = "10.0.2.0/24"
  tags = {
    Name = "pharmacy_subnet_2"
  }
}


################################# CREATE SECURITY GROUP ############################################


resource "aws_db_subnet_group" "pharmacy_db_subnet_group" {
  name       = "pharmacy_db_subnet_group"
  subnet_ids = [aws_subnet.pharmacy_subnet_1.id, aws_subnet.pharmacy_subnet_2.id]

  tags = {
    Name = "pharmacy_db_subnet_group"
  }
}


################################# CREATE DATABASE ############################################


resource "aws_db_instance" "pharmacy_db" {
  identifier           = "pharmacy_db"
  engine               = "mysql"
  engine_version       = "5.7"
  instance_class       = "db.t2.micro"
  allocated_storage    = 20
  name                 = "pharmacy_db"
  username             = "admin"
  password             = "password"
  skip_final_snapshot  = true
  publicly_accessible  = false
  multi_az             = false
  db_subnet_group_name = aws_db_subnet_group.pharmacy_db_subnet_group.name

  tags = {
    cost = "course-work"
  }
}


################################# CREATE S3 BUCKET TO STORE OBJECTS ############################################


resource "aws_s3_bucket" "pharmacy_bucket" {
  bucket = "pharmacy-objects"
  acl    = "public"

  tags = {
    Name = "pharmacy-objects"
  }
}


################################# CREATE AWS GLUE DB ############################################
resource "aws_glue_catalog_database" "pharmacy_db_glue" {
  name = "pharmacy-db-glue"
}


################################# CREATE IAM ROLE FOR AWS GLUE DB ############################################
resource "aws_iam_role" "glue_service_role" {
  name = "AWSGlueServiceRoleDefault"
  assume_role_policy = <<EOF
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Action": "sts:AssumeRole",
        "Principal": {
          "Service": "glue.amazonaws.com"
        },
        "Effect": "Allow",
        "Sid": ""
      }
    ]
  }
  EOF
}


resource "aws_iam_role_policy_attachment" "glue_service_role_policy" {
  role       = aws_iam_role.glue_service_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole"
}


################################# CREATE AWS GLUE - AWS RDS CONNECTION ############################################


resource "aws_glue_connection" "pharmacy-s3-connection" {
  connection_properties = {
    JDBC_CONNECTION_URL = "jdbc:mysql://pharmacy-db.cjpztz68rn7i.eu-central-1.rds.amazonaws.com:3306/pharmacy_shop"
    PASSWORD            = "password"
    USERNAME            = "admin"
  }

  name = "pharmacy_db_connection"

  physical_connection_requirements {
    availability_zone      = "eu-central-1a"
    security_group_id_list = ["sg-07cd918a78abf7940"]
    subnet_id              = "subnet-0e1f46c7e17af2b31"
  }
}


################################# CREATE AWS GLUE CRAWLERS ############################################


resource "aws_glue_crawler" "comments" {
  database_name = "phamacy_glue_db"
  name          = "rds-comments-crawler"
  role          = aws_iam_role.glue_service_role.name

  jdbc_target {
    connection_name = aws_glue_connection.pharmacy-s3-connection.name
    path            = "pharmacy_shop/comments"
  }
}


resource "aws_glue_crawler" "customers" {
  database_name = "phamacy_glue_db"
  name          = "rds-customers-crawler"
  role          = aws_iam_role.glue_service_role.name

  jdbc_target {
    connection_name = aws_glue_connection.pharmacy-s3-connection.name
    path            = "pharmacy_shop/customers"
  }
}


resource "aws_glue_crawler" "discounts" {
  database_name = "phamacy_glue_db"
  name          = "rds-discounts-crawler"
  role          = aws_iam_role.glue_service_role.name

  jdbc_target {
    connection_name = aws_glue_connection.pharmacy-s3-connection.name
    path            = "pharmacy_shop/discounts"
  }
}


resource "aws_glue_crawler" "manufacturers" {
  database_name = "phamacy_glue_db"
  name          = "rds-manufacturers-crawler"
  role          = aws_iam_role.glue_service_role.name

  jdbc_target {
    connection_name = aws_glue_connection.pharmacy-s3-connection.name
    path            = "pharmacy_shop/manufacturers"
  }
}


resource "aws_glue_crawler" "order-items" {
  database_name = "phamacy_glue_db"
  name          = "rds-order-items-crawler"
  role          = aws_iam_role.glue_service_role.name

  jdbc_target {
    connection_name = aws_glue_connection.pharmacy-s3-connection.name
    path            = "pharmacy_shop/order-items"
  }
}


resource "aws_glue_crawler" "packaging" {
  database_name = "phamacy_glue_db"
  name          = "rds-packaging-crawler"
  role          = aws_iam_role.glue_service_role.name

  jdbc_target {
    connection_name = aws_glue_connection.pharmacy-s3-connection.name
    path            = "pharmacy_shop/packaging"
  }
}


resource "aws_glue_crawler" "payments" {
  database_name = "phamacy_glue_db"
  name          = "rds-payments-crawler"
  role          = aws_iam_role.glue_service_role.name

  jdbc_target {
    connection_name = aws_glue_connection.pharmacy-s3-connection.name
    path            = "pharmacy_shop/payments"
  }
}


resource "aws_glue_crawler" "product-categories" {
  database_name = "phamacy_glue_db"
  name          = "rds-product-categories-crawler"
  role          = aws_iam_role.glue_service_role.name

  jdbc_target {
    connection_name = aws_glue_connection.pharmacy-s3-connection.name
    path            = "pharmacy_shop/product-categories"
  }
}


resource "aws_glue_crawler" "products" {
  database_name = "phamacy_glue_db"
  name          = "rds-products-crawler"
  role          = aws_iam_role.glue_service_role.name

  jdbc_target {
    connection_name = aws_glue_connection.pharmacy-s3-connection.name
    path            = "pharmacy_shop/products"
  }
}


resource "aws_glue_crawler" "shippings" {
  database_name = "phamacy_glue_db"
  name          = "rds-shippings-crawler"
  role          = aws_iam_role.glue_service_role.name

  jdbc_target {
    connection_name = aws_glue_connection.pharmacy-s3-connection.name
    path            = "pharmacy_shop/shippings"
  }
}


resource "aws_glue_crawler" "suppliers" {
  database_name = "phamacy_glue_db"
  name          = "rds-suppliers-crawler"
  role          = aws_iam_role.glue_service_role.name

  jdbc_target {
    connection_name = aws_glue_connection.pharmacy-s3-connection.name
    path            = "pharmacy_shop/suppliers"
  }
}


resource "aws_glue_crawler" "orders" {
  database_name = "phamacy_glue_db"
  name          = "rds-orders-crawler"
  role          = aws_iam_role.glue_service_role.name

  jdbc_target {
    connection_name = aws_glue_connection.pharmacy-s3-connection.name
    path            = "pharmacy_shop/orders"
  }
}


resource "aws_glue_crawler" "employee" {
  database_name = "phamacy_glue_db"
  name          = "rds-employee-crawler"
  role          = aws_iam_role.glue_service_role.name

  jdbc_target {
    connection_name = aws_glue_connection.pharmacy-s3-connection.name
    path            = "pharmacy_shop/employee"
  }
}


resource "aws_glue_crawler" "position" {

  database_name = "phamacy_glue_db"
  name          = "rds-position-crawler"
  role          = aws_iam_role.glue_service_role.name

  jdbc_target {
    connection_name = aws_glue_connection.pharmacy-s3-connection.name
    path            = "pharmacy_shop/position"
  }
}


resource "aws_glue_crawler" "work-schedule" {
  database_name = "phamacy_glue_db"
  name          = "rds-work-schedule-crawler"
  role          = aws_iam_role.glue_service_role.name

  jdbc_target {
    connection_name = aws_glue_connection.pharmacy-s3-connection.name
    path            = "pharmacy_shop/work-schedule"
  }
}


################################# CREATE AWS GLUE JOBS ############################################


resource "aws_glue_job" "comments-job" {
  name     = "comments-job"
  role_arn = aws_iam_role.job-role.arn

  command {
    script_location = "s3://aws-glue-scripts-pharmacy/comments-job.py"
  }
}


resource "aws_glue_job" "comments-job" {
  name     = "comments-job"
  role_arn = aws_iam_role.job-role.arn

  command {
    script_location = "s3://aws-glue-scripts-pharmacy/comments-job.py"
  }
}


resource "aws_glue_job" "discounts-job" {
  name     = "discounts-job"
  role_arn = aws_iam_role.job-role.arn

  command {
    script_location = "s3://aws-glue-scripts-pharmacy/discounts-job.py"
  }
}


resource "aws_glue_job" "manufacturers-job" {
  name     = "manufacturers-job"
  role_arn = aws_iam_role.job-role.arn

  command {
    script_location = "s3://aws-glue-scripts-pharmacy/manufacturers-job.py"
  }
}



resource "aws_glue_job" "order-items-job" {
  name     = "order-items-job"
  role_arn = aws_iam_role.job-role.arn

  command {
    script_location = "s3://aws-glue-scripts-pharmacy/order-items-job.py"
  }
}


resource "aws_glue_job" "orders-job" {
  name     = "orders-job"
  role_arn = aws_iam_role.job-role.arn

  command {
    script_location = "s3://aws-glue-scripts-pharmacy/orders-job.py"
  }
}


resource "aws_glue_job" "packaging-job" {
  name     = "packaging-job"
  role_arn = aws_iam_role.job-role.arn

  command {
    script_location = "s3://aws-glue-scripts-pharmacy/packaging-job.py"
  }
}


resource "aws_glue_job" "payments-job" {
  name     = "payments-job"
  role_arn = aws_iam_role.job-role.arn

  command {
    script_location = "s3://aws-glue-scripts-pharmacy/payments-job.py"
  }
}


resource "aws_glue_job" "product-categories-job" {
  name     = "product-categories-job"
  role_arn = aws_iam_role.job-role.arn

  command {
    script_location = "s3://aws-glue-scripts-pharmacy/product-categories-job.py"
  }
}


resource "aws_glue_job" "products-job" {
  name     = "products-job"
  role_arn = aws_iam_role.job-role.arn

  command {
    script_location = "s3://aws-glue-scripts-pharmacy/products-job.py"
  }
}


resource "aws_glue_job" "shippings-job" {
  name     = "shippings-job"
  role_arn = aws_iam_role.job-role.arn

  command {
    script_location = "s3://aws-glue-scripts-pharmacy/shippings-job.py"
  }
}


resource "aws_glue_job" "suppliers-job" {
  name     = "suppliers-job"
  role_arn = aws_iam_role.job-roles.arn

  command {
    script_location = "s3://aws-glue-scripts-pharmacy/suppliers-job.py"
  }
}


resource "aws_glue_job" "employee-job" {
  name     = "employee-job"
  role_arn = aws_iam_role.job-role.arn

  command {
    script_location = "s3://aws-glue-scripts-pharmacy/employee-job.py"
  }
}


resource "aws_glue_job" "work-schedule-job" {
  name     = "work-schedule-job"
  role_arn = aws_iam_role.job-role.arn

  command {
    script_location = "s3://aws-glue-scripts-pharmacy/work-schedule-job.py"
  }
}


resource "aws_glue_job" "position-job" {
  name     = "position-job"
  role_arn = aws_iam_role.job-role.arn

  command {
    script_location = "s3://aws-glue-scripts-pharmacy/position-job.py"
  }
}


################################### CREATE VPC iN THE US REGION #########################################


provider "aws" {
  alias  = "us_east"
  region = "us-east-1"
}


resource "aws_vpc" "pharmacy_replica_vpc" {
  provider   = aws.us_east
  cidr_block = "172.16.0.0/16"

  tags = {
    Name = "pharmacy_replica_vpc"
  }
}


resource "aws_subnet" "pharmacy_replica_subnet" {
  provider   = aws.us_east
  vpc_id     = aws_vpc.pharmacy_replica_vpc.id
  cidr_block = "172.16.1.0/24"

  tags = {
    Name = "pharmacy_replica_subnet"
  }
}


resource "aws_db_subnet_group" "pharmacy_db_replica_subnet_group" {
  provider   = aws.us_east
  name       = "pharmacy_db_replica_subnet_group"
  subnet_ids = [aws_subnet.pharmacy_replica_subnet.id]

  tags = {
    Name = "pharmacy_db_replica_subnet_group"
  }
}


################################### READ REPLICA DATABASE #########################################


resource "aws_db_instance" "pharmacy_db_replica" {
  provider                = aws.us_east
  identifier              = "pharmacy_db_replica"
  replicate_source_db     = aws_db_instance.pharmacy_db.identifier
  instance_class          = "db.t2.micro"
  publicly_accessible     = false
  skip_final_snapshot     = true
  db_subnet_group_name    = aws_db_subnet_group.pharmacy_db_replica_subnet_group.name

  tags = {
    Name = "pharmacy_db_replica"
  }
}


################################### SWITCH REGION #########################################


provider "aws" {
  region = "us-east-1"  # Replace with your desired region
}


################################### CREATE SNS TOPIC #########################################


resource "aws_sns_topic" "object_notification" {
  name = "pharmacy-object-notification"
}


################################### CREATE SNS SUBSCRIPTION #########################################
resource "aws_sns_topic_subscription" "email_subscription" {
  topic_arn = aws_sns_topic.object_notification.arn
  protocol  = "email"
  endpoint  = "one_new_object@pharmacy.com"
}


################################### CREATE SNS NOTIFICATION #########################################


resource "aws_s3_bucket_notification" "object_notification" {
  bucket = "pharmacy-objects"

  topic {
    topic_arn = aws_sns_topic.object_notification.arn
    events    = ["s3:ObjectCreated:*"]
  }
}
