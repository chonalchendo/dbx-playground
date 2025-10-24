terraform {
  required_providers {
    databricks = {
      source = "databricks/databricks"
    }
  }
}

resource "databricks_schema" "bronze" {
  catalog_name = var.catalog_name
  name         = "bronze"
  comment      = "Bronze layer"
  properties = {
    kind = "various"
  }
}

resource "databricks_schema" "silver" {
  catalog_name = var.catalog_name
  name         = "silver"
  comment      = "Silver player"
  properties = {
    kind = "various"
  }
}

resource "databricks_schema" "gold" {
  catalog_name = var.catalog_name
  name         = "gold"
  comment      = "Gold layer"
  properties = {
    kind = "various"
  }
}

resource "databricks_schema" "libraries" {
  catalog_name = var.catalog_name
  name         = "libraries"
  comment      = "Schema to store project artifacts e.g. Python packages."
  properties = {
    kind = "various"
  }
}
