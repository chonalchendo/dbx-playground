terraform {
  required_providers {
    databricks = {
      source = "databricks/databricks"
    }
  }
}

resource "databricks_schema" "sandbox" {
  catalog_name = var.catalog_name
  name         = "sandbox"
  comment      = "this database is managed by terraform"
  properties = {
    kind = "various"
  }
}

resource "databricks_schema" "prod" {
  catalog_name = var.catalog_name
  name         = "prod"
  comment      = "this database is managed by terraform"
  properties = {
    kind = "various"
  }
}
