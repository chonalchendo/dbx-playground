terraform {
  required_providers {
    databricks = {
      source = "databricks/databricks"
    }
  }
}

resource "databricks_job" "job" {
  name = var.job_name
  
  git_source {
    url      = var.repo_url
    provider = "GitHub"
    branch   = var.branch
  }
  
  # Define environment for serverless execution
  environment {
    environment_key = "default"
    spec {
      client = "4"
      dependencies = [
        var.whl_path  # Reference your wheel file
      ]
    }
  }
  
  task {
    task_key        = var.task_key
    environment_key = "default"
    
    spark_python_task {
      python_file = var.script_path
      parameters  = ["--config", var.config_path]
      source      = "GIT"
    }
  }
}