#!/bin/bash
# The purpose of or program is to automate the installation of our packages!

# Install cowsay
#sudo yum install -y cowsay

#echo cowsay installed | cowsay


# Install jq

# sudo yum install -y jq

# echo jq installed | cowsay

for package in cowsay jq tmux git epel sl
do
        sudo yum install $package
        echo $package was installed | cowsay
done

# Install rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
