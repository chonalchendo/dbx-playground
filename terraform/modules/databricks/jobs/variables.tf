variable "job_name" {
  description = "Name of the Databricks job"
  type        = string
}

variable "task_key" {
  description = "Unique key for the task in the job"
  type        = string
}

variable "repo_url" {
  description = "GitHub repo URL containing your job script"
  type        = string
}

variable "branch" {
  description = "Branch of the repo to use"
  type        = string
  default     = "main"
}

variable "script_path" {
  description = "Path to the Python script in the repo"
  type        = string
}

variable "config_path" {
  description = "Path to config file used to configure job"
  type = string
}

variable "whl_path" {
  type        = string
  description = "Path to the wheel file in Databricks volume"
}