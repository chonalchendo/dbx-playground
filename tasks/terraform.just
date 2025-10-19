# Initialize Terraform
[group('terraform')]
terraform-init:
    cd terraform && terraform init

# Plan Terraform changes
[group('terraform')]
terraform-plan:
    cd terraform && terraform init && terraform plan

# Run Terraform
[group('terraform')]
terraform-apply:
    cd terraform && terraform init && terraform apply -auto-approve

# Output Terraform values
[group('terraform')]
terraform-outputs:
    cd terraform && terraform init && terraform output -json > ../feast/terraform_outputs.json

# Destroy cloud resources
[group('terraform')]
terraform-destroy:
    cd terraform && terraform init && terraform destroy -auto-approve
