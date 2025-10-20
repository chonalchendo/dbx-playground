# databricks
variable "pat_token" {
  type        = string
  description = "Databricks personal access token (PAT)"
}

variable "hostname" {
  type        = string
  description = "Databricks hostname"
}

# aws
variable "aws_region" {
  type        = string
  description = "The AWS region the project deploys to."
}

variable "project_name" {
  type        = string
  description = "The project name."
}

variable "bucket_name" {
  type = string
  description = "The project bucket name"
}