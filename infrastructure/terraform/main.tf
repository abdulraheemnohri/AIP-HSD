# AIP-HSD Infrastructure-as-Code (Terraform)
# Stub for provisioning cloud resources (e.g., AWS, Azure, GCP)

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "aiphsd_backend" {
  ami           = "ami-0c55b159cbfafe1f0" # Ubuntu 22.04 LTS
  instance_type = "t3.large"
  tags = {
    Name = "AIP-HSD-Backend-Server"
  }
}

resource "aws_db_instance" "aiphsd_db" {
  allocated_storage    = 20
  db_name              = "aiphsd"
  engine               = "postgres"
  engine_version       = "15.4"
  instance_class       = "db.t3.micro"
  username             = "admin"
  password             = "supersecretpassword"
  skip_final_snapshot  = true
}
