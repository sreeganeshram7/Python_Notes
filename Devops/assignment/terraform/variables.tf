variable "aws_region" {
  type    = string
  default = "ap-south-1"
}

variable "bucket_name" {
  type        = string
  description = "AmazonS3FullAccess"
}

variable "instance_type" {
  type    = string
  default = "t2.micro"
}

variable "key_name" {
  type        = string
  description = "ec2_instance"
}
