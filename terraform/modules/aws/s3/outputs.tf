output "project_bucket_name" {
  value = var.project_bucket_name
}

output "project_bucket_arn" {
  value = aws_s3_bucket.project_bucket.arn
}