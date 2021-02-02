terraform {
  backend "remote" {
      hostname ="app.terraform.io"
      organization="huyeduon"
      workspaces {
        name = "cloudcode"
      }
  }
}

provider "aws" {
    region = "us-east-1"
    access_key = var.aws_acc_key
    secret_key = var.aws_sec_key
}

resource "aws_s3_bucket" "test" {
    bucket_prefix = "test-"
}
