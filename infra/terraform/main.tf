# NeuroOps AWS infrastructure. Do not run terraform apply without user approval.
# Required: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY (or profile); ask user.

terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  backend "s3" {
    # Optional: uncomment and set bucket/key for remote state
    # bucket = "neuroops-tfstate"
    # key    = "neuroops/terraform.tfstate"
    # region = "us-east-1"
  }
}

provider "aws" {
  region = var.aws_region
}

# Placeholder resources: uncomment and customize when deploying with user approval.

# data "aws_availability_zones" "available" {}
# resource "aws_vpc" "main" { ... }
# resource "aws_subnet" "private" { count = 2; ... }
# resource "aws_eks_cluster" "main" { ... }
# resource "aws_db_instance" "postgres" {
#   identifier     = "${var.project_name}-${var.environment}"
#   engine         = "postgres"
#   instance_class = var.db_instance_class
#   allocated_storage = var.db_allocated_storage
#   username = var.db_username
#   password = var.db_password
#   ...
# }
# resource "aws_s3_bucket" "artifacts" { ... }

output "region" {
  value = var.aws_region
}

output "message" {
  value = "Terraform placeholder. Configure resources in main.tf and run apply only after user approval."
}
