output "instance_public_ip" {
  value       = aws_instance.builder.public_ip
  description = "The public IP of ${var.owner}'s EC2 instance"
}

output "ssh_key_path" {
  value       = local_file.private_key.filename
  description = "The path to ${var.owner}'s SSH private key"
}

output "security_group_id" {
  value       = aws_security_group.builder_sg.id
  description = "The ID of ${var.owner}'s security group"
}

output "ssh_connection_command" {
  value       = "ssh -i ${local_file.private_key.filename} ec2-user@${aws_instance.builder.public_ip}"
  description = "Command to SSH into ${var.owner}'s EC2 instance"
} 