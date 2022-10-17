#!/bin/bash
echo "The purpose of this program is to connect to the aws virtual machine"
echo "This script must be run in the same directory as your .pem file"
echo "Your .pem file must be called labsuser.pem"

echo "Enter the AWS EC2 virtual machine IP Address:"
read varip
echo
echo "After connecting, run the the following command:"
echo "curl -s https://raw.githubusercontent.com/kris-classes/restart/main/aws_vm_initscript.sh | sh && exec zsh -l"
echo
echo "Connecting..."
echo
ssh -i ./labsuser.pem ec2-user@$varip