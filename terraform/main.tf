
data "databricks_current_user" "me" {}
data "databricks_spark_version" "latest" {}
data "databricks_node_type" "smallest" {
  local_disk = true
}

# databricks modules
module "notebook" {
  source = "./modules/databricks/notebooks"
  home   = data.databricks_current_user.me.home
}

module "schema" {
  source       = "./modules/databricks/schemas"
  catalog_name = "workspace"
}

module "dbx_playground_library" {
  source         = "./modules/databricks/libraries"
  catalog_name   = "workspace"
  schema_name    = "prod"
  volume_name    = "volume"
  whl_local_path = "${path.module}/../dist/dbx_playground-0.1.0-py3-none-any.whl"
}

# aws modules
module "s3" {
  source              = "./modules/aws/s3"
  project_name        = var.project_name
  project_bucket_name = var.bucket_name
}

module "iam" {
  source            = "./modules/aws/iam"
  project_name      = var.project_name
  project_user_name = var.project_name
  # Bucket ARNs from S3 module
  project_bucket_arn = module.s3.project_bucket_arn
}
