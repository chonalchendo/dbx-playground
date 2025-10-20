terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

# s3 bucket for raw transactions data
resource "aws_s3_bucket" "project_bucket" {
  bucket = var.project_bucket_name
}
