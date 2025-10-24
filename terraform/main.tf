
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
  schema_name    = "libraries"
  volume_name    = "volume"
  whl_local_path = "${path.module}/../dist/dbx_playground-0.1.0-py3-none-any.whl"
}

module "bronze_ingestion_job" {
  source = "./modules/databricks/jobs"
  job_name = "bronze_ingestion_job"
  task_key = "bronze_load_task"
  repo_url = "https://github.com/chonalchendo/dbx-playground.git"
  branch = "main"
  script_path = "src/dbx_playground/jobs/ingestion.py"
  config_path = "confs/ingestion.yaml"
  whl_path = module.dbx_playground_library.whl_path
  depends_on = [ module.dbx_playground_library ]
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
