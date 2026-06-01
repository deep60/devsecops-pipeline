# terraform/main.tf — intentionally misconfigured for demo

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# ❌ S3 bucket with public access — Checkov will catch this
resource "aws_s3_bucket" "data" {
  bucket = "my-company-data-bucket"
  acl    = "public-read"          # CRITICAL: world-readable bucket
}

# ❌ Security group allowing all inbound traffic
resource "aws_security_group" "open" {
  name = "allow-all"

  ingress {
    from_port   = 0
    to_port     = 65535
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # CRITICAL: open to entire internet
  }
}

# ❌ RDS with no encryption and public access
resource "aws_db_instance" "main" {
  identifier        = "prod-database"
  engine            = "mysql"
  instance_class    = "db.t3.micro"
  username          = "admin"
  password          = "password123"   # hardcoded password
  storage_encrypted = false           # no encryption at rest
  publicly_accessible = true          # exposed to internet
  skip_final_snapshot = true
}

# ❌ EC2 instance with overly permissive IAM
resource "aws_iam_role" "ec2_role" {
  name = "ec2-full-access"

  assume_role_policy = jsonencode({
    Statement = [{
      Action    = "*"              # wildcard — full AWS access
      Effect    = "Allow"
      Principal = { Service = "ec2.amazonaws.com" }
    }]
  })
}
