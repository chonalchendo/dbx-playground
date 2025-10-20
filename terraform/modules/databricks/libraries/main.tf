terraform {
  required_providers {
    databricks = {
      source = "databricks/databricks"
    }
  }
}

resource "databricks_volume" "libs" {
  name         = var.volume_name
  catalog_name = var.catalog_name
  schema_name  = var.schema_name
  volume_type  = "MANAGED"
}

resource "databricks_file" "whl" {
  source = var.whl_local_path
  path   = "/Volumes/${var.catalog_name}/${var.schema_name}/${var.volume_name}/${basename(var.whl_local_path)}"
  depends_on = [
    databricks_volume.libs
  ]
}
