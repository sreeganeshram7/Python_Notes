output "bucket_name" {
  value = aws_s3_bucket.simulator_bucket.bucket
}

output "ec2_public_ip" {
  value = aws_instance.web.public_ip
}
