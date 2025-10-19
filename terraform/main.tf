provider "databricks" {
  host  = var.hostname
  token = var.pat_token
}

data "databricks_current_user" "me" {}
data "databricks_spark_version" "latest" {}
data "databricks_node_type" "smallest" {
  local_disk = true
}

resource "databricks_notebook" "this" {
  path     = "${data.databricks_current_user.me.home}/Terraform"
  language = "PYTHON"
  content_base64 = base64encode(<<-EOT
    # created from ${abspath(path.module)}
    display(spark.range(10))
    EOT
  )
}

resource "databricks_notebook" "test" {
  source = "../notebooks/test.ipynb"
  path   = "${data.databricks_current_user.me.home}/test"
}

resource "databricks_notebook" "test_2" {
  source = "../notebooks/test_2.py"
  path   = "${data.databricks_current_user.me.home}/test_2"
}

resource "databricks_schema" "sandbox" {
  catalog_name = "workspace"
  name         = "sandbox"
  comment      = "this database is managed by terraform"
  properties = {
    kind = "various"
  }
}

resource "databricks_schema" "prod" {
  catalog_name = "workspace"
  name         = "prod"
  comment      = "this database is managed by terraform"
  properties = {
    kind = "various"
  }
}

output "notebook_url" {
  value = databricks_notebook.this.url
}

output "databricks_schema_id" {
  value = databricks_schema.sandbox.id
}
