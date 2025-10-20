variable "volume_name" {
  description = "Name of the Databricks volume"
  type        = string
}

variable "catalog_name" {
  description = "Catalog where the volume will be created"
  type        = string
}

variable "schema_name" {
  description = "Schema name under the catalog"
  type        = string
}

variable "whl_local_path" {
  description = "Path to the local wheel file to upload"
  type        = string
}
