resource "databricks_volume" "libs" {
  name         = "volume"
  catalog_name = "workspace"
  schema_name  = "prod"
  volume_type  = "MANAGED"
}

resource "databricks_file" "dbx_playground_whl" {
  source = "${path.module}/../dist/dbx_playground-0.1.0-py3-none-any.whl"
  path   = "/Volumes/workspace/prod/volume/dbx_playground-0.1.0-py3-none-any.whl"
}
