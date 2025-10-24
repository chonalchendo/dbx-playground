output "bronze_schema_id" {
  value = databricks_schema.bronze.id
}

output "silver_schema_id" {
  value = databricks_schema.silver.id
}

output "gold_schema_id" {
  value = databricks_schema.gold.id
}

output "libraries_schema_id" {
  value = databricks_schema.libraries.id
}