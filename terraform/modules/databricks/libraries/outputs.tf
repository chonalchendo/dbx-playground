output "wheel_path" {
  value = databricks_file.whl.path
}

output "volume_uri" {
  value = databricks_volume.libs.name
}