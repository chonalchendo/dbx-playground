terraform {
  required_providers {
    databricks = {
      source = "databricks/databricks"
    }
  }
}

resource "databricks_notebook" "this" {
  path     = "${var.home}/Terraform"
  language = "PYTHON"
  content_base64 = base64encode(<<-EOT
    # created from ${abspath(path.module)}
    display(spark.range(10))
  EOT
  )
}

resource "databricks_notebook" "test" {
  source = "../notebooks/test.ipynb"
  path   = "${var.home}/test"
}

resource "databricks_notebook" "test_2" {
  source = "../notebooks/test_2.py"
  path   = "${var.home}/test_2"
}